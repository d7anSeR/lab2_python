import os
import csv


class Iterator1:
    def __init__(self, path_file):
        self.count = 0
        self.files = os.listdir(os.path.join("dataset", path_file))
        self.limit = len(self.files)
        self.path = path_file
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            obj = self.files[self.count]
            self.count += 1
            return obj
        raise StopIteration


class Iterator2:
    def __init__(self, class_n,  path_file):
        self.files = os.listdir(path_file)
        for elem in self.files:
            if not class_n in elem:
                self.files.remove(elem)
        self.limit = len(self.files)
        self.count = 0
        self.path = path_file

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            obj = self.files[self.count]
            self.count += 1
            return obj
        raise StopIteration


class IteratorTask3:
    def __init__(self, class_name, path, annotation_n):
        self.files = []
        with open(os.path.join(path, annotation_n), encoding='UTF-16') as f:
            reader = csv.reader(f, delimiter=';')
            for elem in reader:
                if elem[2] == class_name:
                    self.files.append(os.path.basename(elem[0]))
        pass
        self.limit = len(self.files)
        self.count = 0
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            obj = self.files[self.count]
            self.count += 1
            return obj
        raise StopIteration
