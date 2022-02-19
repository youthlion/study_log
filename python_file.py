import os
from pathlib import Path

root_name=Path("./data/input")

#列举目录里的文件名,root_path为Path类
def listpath(root_path):
    names=os.listdir(root_path)
    file_names=list()
    for name in names:
        file_names.append(Path.joinpath(root_path,name))
    return file_names
