import os
import glob
import shutil

files = glob.glob("*.log")

with open(files[0],"r") as outfile:
    data = outfile.readlines()

for linenum, line in enumerate(data):
    if "Standard orientation" in line:
        finalnum = linenum

words = data[(finalnum+5):]

for line in words:
    if "--" in line:
        break
    else:
        linelist = line.split()
        if linelist[1] == "47":
            del linelist[0:3]
            linelist.insert(0, "Ag")
            line = linelist[0] + " " + linelist[1] + " " + linelist[2] + " " + linelist[3]
        if linelist[1] == "13":
            del linelist[0:3]
            linelist.insert(0, "Al")
            line = linelist[0] + " " + linelist[1] + " " + linelist[2] + " " + linelist[3]
        if linelist[1] == "21":
            del linelist[0:3]
            linelist.insert(0, "Sc")
            line = linelist[0] + " " + linelist[1] + " " + linelist[2] + " " + linelist[3]
        print(line)

