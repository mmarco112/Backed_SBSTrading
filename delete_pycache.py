import os

globalFolder = ""
BetfairFolder = ""
DirettaFolder = ""
PinnacleFolder = ""

AllCacheFolders = [globalFolder, BetfairFolder, DirettaFolder, PinnacleFolder]


for i in AllCacheFolders:
    if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    else:
    print("The file does not exist")