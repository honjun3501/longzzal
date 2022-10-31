import os
from pathlib import Path
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def do_print(path):
    print(f'{path} : ', path)

print(os.path.join('user','Desktop','Python'))
print(os.getcwd())


print(os.path.join(os.getcwd(), 'Python'))


file_folder = Path('grid_demo_img/')
do_print((file_folder))

result = str(file_folder / 'demo_frame.png')
do_print(result)
result = resource_path(result)
do_print(result)




filepath = os.getcwd()
file_name = filepath[:-4] + "/frame%s.{}".format(args[1]) % args[2].zfill(5)
result = str(Path(file_name))