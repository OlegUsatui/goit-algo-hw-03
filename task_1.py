import sys
from pathlib import Path
import shutil

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def get_input_path():
    # Ask user for the source directory path
    source_dir_input = input("Будь ласка, введіть шлях до початкової директорії: ").strip()
    source_dir = Path(source_dir_input)

    if not source_dir.is_dir():
        print("Помилка: Невірний шлях до директорії джерела.")
        sys.exit(1)

    # Default destination directory name
    dest_dir_input = input("Будь ласка, введіть шлях до директорії призначення (залиште порожнім для 'dist'): ").strip()
    dest_dir = Path(dest_dir_input) if dest_dir_input else Path("dist")

    return source_dir, dest_dir

def copy_file_to_dest(file_path, dest_dir):
    if not file_path.is_file():
        return

    file_extension = file_path.suffix[1:]  # Get extension without the dot
    if not file_extension:  # Handle files without an extension
        file_extension = "no_extension"
    target_dir = dest_dir / file_extension

    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(file_path, target_dir / file_path.name)
    except Exception as e:
        print(f"Помилка при копіюванні файлу {file_path}: {e}")

def process_directory(directory, dest_dir):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                process_directory(item, dest_dir)
            else:
                copy_file_to_dest(item, dest_dir)
    except Exception as e:
        print(f"Помилка при обробці директорії {directory}: {e}")

def main():
    source_dir, dest_dir = get_input_path()
    process_directory(source_dir, dest_dir)

if __name__ == "__main__":
    main()