from task1 import run1
from task2 import run2
from task3 import run3
from task4 import output_elem

if __name__ == '__main__':
    # run1("good", "bad", "annotation1.csv")
    # run2("new_dir_task2", "good", "bad", "annotation2.csv")
    # run3("new_dir_task3", "good", "bad", "annotation3.csv")
    for i in output_elem("good"):
        print("good", i)
    for i in output_elem("bad"):
        print("bad", i)
    print("4 task completed")
# во всех файлах прописать docstring-и
