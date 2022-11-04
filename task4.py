import os


def output_elem(folder_name) -> str:
    files = os.listdir(os.path.join("dataset", folder_name))
    files.append(None)
    i = 0
    for i in range(0, len(files) + 1):
        yield files[i]