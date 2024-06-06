# Task: Automate a Task
#
# Identify a repetitive task, such as data
# processing, file management, or report
# generation, and develop a script to
# automate it using Python. This task will
# showcase their problem-solving skills and
# familiarity with Python's automation
# capabilities.
import os
import shutil

path = r"C:/Users/ASUS/Desktop/Python Programs/Programs/Cognifyz Technologies Python projects/Level 3/Automated Task/"
file = os.listdir(path)
# print(file)
folder = ['Excel Files', 'Image Files', 'Ppt Files', 'Text Files', 'Word Files']
for i in range(0, len(folder)):
    if not os.path.exists(path + folder[i]):
        print(path + folder[i])
        os.makedirs(path + folder[i])
for i in file:
    if ".xlsx" in i and not os.path.exists(path + "Excel Files/" + i):
        shutil.move(path+i, path + "Excel Files")
    if ".png" in i and not os.path.exists(path + "Image Files/" + i):
        shutil.move(path+i, path + "Image Files")
    if ".pptx" in i and not os.path.exists(path + "Ppt Files/" + i):
        shutil.move(path+i, path + "Ppt Files")
    if ".txt" in i and not os.path.exists(path + "Text Files/" + i):
        shutil.move(path+i,path + "Text Files")
    if ".docx" in i and not os.path.exists(path + "Word Files/" + i):
        shutil.move(path+i, path + "Word Files")
    else:
        print("No more files to move")
# print(file)
