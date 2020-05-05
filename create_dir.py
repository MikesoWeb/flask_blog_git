import os

path = r'C:\Users\z\Desktop\create_func_dirs\45\67'

if not os.path.exists(path):
    os.makedirs(path)
    print(f'Указанный вами путь был создан: {path}')