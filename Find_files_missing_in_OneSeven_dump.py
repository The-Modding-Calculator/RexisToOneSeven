import os
import sys
import shutil

if not (len(sys.argv) > 3):
    print("Usage: {} <look up table> <Rexis Upscaled Textures dir> <output dir>".format(sys.argv[0]))
    sys.exit(0)

lookUpFile = open(sys.argv[1], "r")
lookUpTable = lookUpFile.read().split("\n")
lookUpFile.close()
if lookUpTable[-1] == "":
    lookUpTable.pop(-1)
RexisReplcementTexPath = sys.argv[2]

missingDumps = sys.argv[3]

#Empty PNGs from missingDumps
for file in os.listdir(missingDumps):
    if file.split(".")[1].lower() == "png":
        os.remove(os.path.join(missingDumps, file))

for root, _, files in os.walk(RexisReplcementTexPath):
    for fullFileName in files:
        #Find hash in file name
        hashFileName = fullFileName
        if "_" in hashFileName:
            hashFileName = hashFileName.split("_")[1]
        if "-" in hashFileName:
            hashFileName = hashFileName.split("-")[0]
        if ".png" in hashFileName:
            hashFileName = hashFileName.split(".")[0]

        foundTexInDump = False
        for hashes in lookUpTable:
            if hashFileName in hashes.split(", ")[0]:
                foundTexInDump = True
                break
        if not foundTexInDump:
            print(fullFileName, "was missing in dump")
            shutil.copy(os.path.join(root, fullFileName), os.path.join(missingDumps, fullFileName))
