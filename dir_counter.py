import os
from sys import argv
 
if __name__ == '__main__':
    top = argv[1]
    total_files = 0
    total_lines = 0
    total_words = 0
    total_bytes = 0
 
    for path, dirs, files in os.walk(top):
        total_files += len(files)
        for fname in files:
            fpath = os.path.join(path, fname)
            try:
                with open(fpath) as fh:
                    for line in fh:
                        total_lines += 1
                        total_words += len(line.split())
                        total_bytes += len(bytes(line, 'utf-8'))
            except:
                print('unicode error')
                pass
 
    print(f'{total_lines} lines')
    print(f'{total_files} files')