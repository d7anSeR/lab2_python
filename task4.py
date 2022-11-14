import os
from typing import Optional


def output_elem(folder_name : str) -> Optional[str]:
    '''The function returns the name of the file with the values of local variables saved'''
    files = os.listdir(os.path.join("dataset", folder_name))
    files.append(None)
    i = 0
    for i in range(0, len(files) + 1):
        yield files[i]
