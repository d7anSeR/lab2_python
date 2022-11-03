import csv
import os
import shutil
from random import randint

# узнать по поводу аннотации для 2,3 и ... заднаий : нужно для каждого csv файла прописывать полный путь и тд?


def dir_create(dir_name) -> None:
    name_dir_folder = os.path.join(dir_name, "dataset")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    if not os.path.isdir(name_dir_folder):
        name = os.path.join(dir_name, "dataset")
        os.mkdir(name)


def copy_dir(dir_name, good_name, bad_name, annotation_name) -> None:
    dir_create(dir_name)
    good = os.path.join("dataset", good_name)
    bad = os.path.join("dataset", bad_name)
    list_good = os.listdir(good)
    list_bad = os.listdir(bad)
    list_tmp = []
    for file_dataset in os.listdir("dataset"):
        path_p = os.path.join("dataset", file_dataset)
        class_name = os.listdir(path_p)
        for elem in class_name:
            flag = True
            number = randint(0, 10000)
            while flag:
                if number in list_tmp:
                    number = randint(0, 10000)
                else:
                    list_tmp.append(number)
                    flag = False
            old_file = os.path.join(path_p, elem)
            new_file = os.path.join(
                dir_name, "dataset", f"{number}.txt")
            shutil.copy(old_file, new_file)
            with open(annotation_name, mode="a", encoding="UTF-16", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                result_file = os.path.join("dataset", f"{number}.txt")
                writer.writerow([file_dataset, result_file])
            pass
    print("3 task completed")


def run3(dir_name, good_name, bad_name, annotation_name) -> None:
    copy_dir(dir_name, good_name, bad_name, annotation_name)
