import argparse
import os
import time
import shutil


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trash_folder_path')
    parser.add_argument('--age_thr')
    parser = parser.parse_args()
    return parser.trash_folder_path, int(parser.age_thr)


def get_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def get_dirs(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def remove_dirs_without_files(folder_path, log_file) -> bool:
    if len(os.listdir(folder_path)) == 0:
        return True
    exist_files = len(get_files(folder_path)) != 0
    empty_dirs = []
    for next_dir in get_dirs(folder_path):
        is_empty = remove_dirs_without_files(os.path.join(folder_path, next_dir), log_file)
        if is_empty:
            empty_dirs.append(next_dir)
    if exist_files or len(empty_dirs) != len(get_dirs(folder_path)):
        for next_dir in empty_dirs:
            log_file.write(f'{os.path.join(folder_path, next_dir)} deleted by empty\n')
            shutil.rmtree(os.path.join(folder_path, next_dir))
        return False
    return True


def remove_empty_dirs(folder_path, log_file):
    for root, dirs, files in os.walk(folder_path):
        if root == folder_path:
            continue
        if len(files) == 0 and len(dirs) == 0:
            print(root, dirs, files)
            log_file.write(f'{root} deleted by empty\n')
            os.rmdir(root)


def get_file_age(path):
    return time.time() - os.path.getatime(path)


def remove_files(path, life_time, log_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            delta_time = get_file_age(os.path.join(root, file))
            if delta_time > life_time:
                log_file.write(f'{os.path.join(root, file)} deleted by life time\n')
                os.remove(os.path.join(root, file))


def check_trash_folder(path, life_time, log_file, rmdir_nofiles=False):
    os.chdir(path)
    remove_files(path, life_time, log_file)
    if rmdir_nofiles:
        remove_dirs_without_files(path, log_file)
    else:
        remove_empty_dirs(path, log_file)


if __name__ == '__main__':
    path, life_time = get_args()
    with open('clean_trash.log', 'w+') as f:
        while True:
            check_trash_folder(path, life_time, f)
            time.sleep(1)
