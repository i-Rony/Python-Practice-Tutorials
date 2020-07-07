import os

# Delete a File from System 
fileName = "../Python-Repo/Python-Advance-Tutorial/FileHandling/TestFiles/DeleteMe.txt"
if os.path.exists(fileName) :
    os.remove(fileName)
else :
    print("File Doesn't Exsits")

# Delete a directory from System 
path = "../Python-Repo/Python-Advance-Tutorial/FileHandling/DeleteMe"
os.rmdir(path)