import os
import json


def write_dict(path : str, my_dict):
    with open(path, "w", encoding="utf8") as f:
        f.write(json.dumps(my_dict))
    return


write_dict("file.txt", {"ex": 1, "chpeks": 2})


def read_dict(path: str):
    with open(path, encoding="utf8") as f:
        data = json.load(f)
    return data


print(read_dict("menu.json"))


def ls(path="./"):
    list_file = os.listdir('./')
    coll_file = 0
    coll_dir = 0
    for file in list_file:
        if os.path.isfile(path+file):
            print(file)
            coll_file += 1
        elif os.path.isdir(path+file):
            print("|"+file)
            coll_dir += 1
    print(f"По данному пути Файлов - {coll_file}шт. Папок - {coll_dir}шт.")


ls()
