import os
import sys
import shutil

if not (len(sys.argv) > 3):
    print("Usage: renxxh.py <multi hash textures dir> <Rexis replacement textures dir> <output dir>")
    sys.exit(0)

multiHashPath = sys.argv[1]
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
        for multiHashFile in os.listdir(multiHashPath):
            if hashFileName in multiHashFile:
                foundTexInDump = True
                break
        if not foundTexInDump:
            print(fullFileName, "was missing in dump")
            shutil.copy(os.path.join(root, fullFileName), os.path.join(missingDumps, fullFileName))
