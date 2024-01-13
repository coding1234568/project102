import os
import shutil

from_directory = "C:/Users/udaya/Desktop/project102"
to_directory = "C:/Users/udaya/Desktop/project102"

files = os.listdir(from_directory)
print(files)

for file in files:
    name,extention = os.path.splitext(file)
    print(name,extention)

    if extention == ".pdf":
        p1 = from_directory + "/" + file
        p2 = to_directory + "/" + "Documents"
        p3 = to_directory + "/" + "Documents" + "/" + file

        if os.path.exists(p2):
            shutil.move(p1,p3)

        else:
            os.makedirs(p2)
            shutil.move(p1,p3)

    if extention == ".txt":
        p1 = from_directory + "/" + file
        p2 = to_directory + "/" + "txt documents"
        p3 = to_directory + "/" + "txt documents" + "/" + file

        if os.path.exists(p2):
            shutil.move(p1,p3)

        else:
            os.makedirs(p2)
            shutil.move(p1,p3)

    if extention == ".png":
        p1 = from_directory + "/" + file
        p2 = to_directory + "/" + "Images"
        p3 = to_directory + "/" + "Images" + "/" + file

        if os.path.exists(p2):
            shutil.move(p1,p3)

        else:
            os.makedirs(p2)
            shutil.move(p1,p3)