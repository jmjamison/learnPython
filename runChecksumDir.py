#!/usr/bin/python
#
# This creates a file, named: today's date_bkup_directory_checksumList.txt
#       that lists each file in the directory and it's checksum
#     15feb13jmj - runs from the directory to be checked
#
# 20181119jmj fix code for python 3.7x - change print statements and add the uft-8 encoding line 25
# this version, python 3.7 reads external dir
#

import os, sys, os.path, hashlib, datetime

directoryToCheck = input("Directory to checksum: ")

if os.path.isdir(directoryToCheck): 
    print(directoryToCheck)

else:
    print(directoryToCheck + " is not a directory, try again")

pathString = directoryToCheck.split(os.path.sep)

fileDirectory = pathString[len(pathString)-1]
print(fileDirectory)


dirs = os.listdir( directoryToCheck )


outfile = open(fileDirectory + "_" + str(datetime.date.today()) + "_" + "_checksumList.txt", "a+")
print(outfile)

# This would print all the files and directories
for file in dirs:
   checksumValue = hashlib.sha1(str(file).encode('utf-8')).hexdigest()   
   outfile.write("\n" + file + ": " + checksumValue)
   #print("\n" + file)

outfile.close()
