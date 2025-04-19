import argparse
import os
from fnmatch import fnmatch


def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_dir', help='trash folder path', required=True)
    dir_path = parser.parse_args().project_dir
    return dir_path


def get_gitignore(dir_path):
    dir_path = os.path.join(dir_path, '.gitignore')
    r_patterns = []
    f_patterns = []
    with open(dir_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == '*':
                r_patterns.append(line)
            else:
                f_patterns.append(line)
    return r_patterns, f_patterns


def fits(path, file, pattern):
    return fnmatch(os.path.join(path, file), pattern)


def check_r_patterns(path, r_patterns):
    for pattern in r_patterns:
        for root, dirs, files in os.walk(path):
            for file in files:
                if fits(root, file, pattern):
                    print(f'{os.path.join(root[len(path) + 1:], file)} ignored by expression {pattern}')


def check_f_patterns(path, f_patterns):
    for pattern in f_patterns:
        if os.path.exists(os.path.join(path, pattern)):
            print(f'{pattern} ignored by expression {pattern}')


if __name__ == '__main__':
    path = get_path()
    os.chdir(path)
    r_patterns, f_patterns = get_gitignore(path)
    print('Ignored files:')
    check_r_patterns(path, r_patterns)
    check_f_patterns(path, f_patterns)
