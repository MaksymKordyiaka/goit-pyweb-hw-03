import os
import shutil
import sys
from multiprocessing import Pool

def copy_file(source_file, dest_dir):
    # Копіює файл у цільову директорію.
    shutil.copy(source_file, dest_dir)

def process_directory(args):
    # Обробляє директорію рекурсивно і копіює файли до цільової директорії.
    source_dir, dest_dir = args
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            extension = os.path.splitext(file)[1].lower()
            if extension:
                dest_subdir = os.path.join(dest_dir, extension[1:])
                os.makedirs(dest_subdir, exist_ok=True)
                copy_file(source_file, dest_subdir)

def main():
    # Отримати джерельну та цільову директорії з аргументів командного рядка
    source_dir = sys.argv[1] if len(sys.argv) > 1 else "Хлам"
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Створити цільову директорію, якщо вона не існує
    os.makedirs(dest_dir, exist_ok=True)

    # Обробити файли використовуючи багатопоточність
    pool = Pool()
    pool.map(process_directory, [(source_dir, dest_dir)])
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
