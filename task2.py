import csv
import os
import shutil


def dir_create(dir_name) -> None:
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def copy_dir(dir_name, good_name, bad_name, annotation_name) -> None:
    dir_create(dir_name)
    good = os.path.join("dataset", good_name)
    bad = os.path.join("dataset", bad_name)
    list_good = os.listdir(good_name)
    list_bad = os.listdir(bad_name)
    for file_dataset in os.listdir("dataset"):
        path_p = os.path.join("dataset", file_dataset)
        class_name = os.listdir(path_p)
        for elem in class_name:
            old_file = os.path.join(path_p, elem)
            new_file = os.path.join(
                dir_name, "dataset", f"{file_dataset}_{elem}")
            shutil.copy(old_file, new_file)
        with open(annotation_name, mode="w", encoding="UTF-16", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            for elem in os.path.join(dir_name, "dataset"):
                writer.writerow([file_dataset, f"{file_dataset}_{elem}"])
        pass


def run2(dir_name, good_name, bad_name, annotation_name) -> None:
    copy_dir(dir_name, good_name, bad_name, annotation_name)