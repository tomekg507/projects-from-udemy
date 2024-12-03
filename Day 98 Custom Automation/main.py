import os

PATH = '/home/tomek/Downloads'
all_files = os.listdir(PATH)

all_ext = [file.split('.')[-1] for file in all_files if len(file.split('.')) > 1]

unique_ext = list(set(all_ext))

for ext in unique_ext:
    try:
        os.mkdir(f'{PATH}/{ext}')
    except FileExistsError:
        pass

for file in all_files:
    if len(file.split('.')) > 1:
        file_ext = file.split('.')[-1]
        os.rename(f'{PATH}/{file}', f'{PATH}/{file_ext}/{file}')

print(unique_ext)