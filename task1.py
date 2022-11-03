import csv
import os


def writing_csv(name_class_good, name_class_bad, name_annatation) -> None:
    with open(name_annatation, mode="w", encoding="UTF-16", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        name_good_otnos = os.path.join("dataset", name_class_good)
        name_bad_otnos = os.path.join("dataset", name_class_bad)
        list_good = os.listdir(name_class_good)
        list_bad = os.listdir(name_class_bad)
        for elem in list_good:
            abspath_good = os.path.abspath(name_class_good)
            writer.writerow([abspath_good, name_good_otnos, name_class_good])
        for elem in list_bad:
            abspath_bad = os.path.abspath(name_class_bad)
            writer.writerow([abspath_bad, name_bad_otnos, name_class_bad])
    pass


def run1(name_class_good, name_class_bad, name_annatation) -> None:
    writing_csv(name_class_good, name_class_bad, name_annatation)