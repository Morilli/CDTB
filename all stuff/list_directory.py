import os
import sys

mylist = os.listdir(sys.argv[1])
with open("./directory_list.txt", "w+") as out_file:
    for a in mylist:
        out_file.write(f"{a.split('.')[0]}\n")
