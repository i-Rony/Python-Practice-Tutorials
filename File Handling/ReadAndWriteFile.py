# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# Read and Write File


fileName = "../Python-Repo/Python-Advance-Tutorial/FileHandling/TestFiles/Test.txt"
read = open(fileName,"r")
print(read.read())

write = open(fileName,"a")
write.write("\nCreated By Arun Ammasai")
write.close()

updatedFile = open(fileName,"r")
print(updatedFile.read())
updatedFile.close()

overWrite = open(fileName,"w") # Override the Content
overWrite.write("\nContent Removed")
overWrite.close()

readOverWrite = open(fileName,"r")
readOverWrite.read()





