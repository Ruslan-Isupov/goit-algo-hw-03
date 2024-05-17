import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description="Copy files to folder")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Folder with files"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("dist"), help="Folder for coping"
    )
    return parser.parse_args()

def recursive_copy(source: Path, output: Path):
    try:
        for element in source.iterdir():
            if element.is_dir():
                recursive_copy(element, output)
            else:
                ext = element.suffix[1:]
                folder = output / ext
                folder.mkdir(parents=True, exist_ok=True)
                shutil.copy(element, folder)
    except Exception as e:
        print(f"Error copying file: {e}")

def main():
    args = parse_argv()
    # print(args.output)
    # args.output.mkdir(parents=True, exist_ok=True) # Створюємо директорію призначення якщо вона не існує
    recursive_copy(args.source, args.output)
    

if __name__ == "__main__":
    main()

# python exerc_1.py -s D:\check_path -o D:\copy_path
