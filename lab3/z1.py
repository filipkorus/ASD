import glob
import os

if __name__ == '__main__':
    files = glob.glob('zadanie1/*')
    for file in files:
        file_name = file.split('\\')[1]
        try:
            os.mkdir(f'zadanie1/{file_name[0].upper()}')
        except FileExistsError:
            pass
        os.rename(file, f'zadanie1/{file_name[0].upper()}/{file_name}')
