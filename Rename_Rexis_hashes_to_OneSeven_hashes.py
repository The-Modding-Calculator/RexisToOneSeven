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
RexisHashPath = sys.argv[2]

renamedOutput = sys.argv[3]

##I'm not sure if I should remove this all together just yet
#missingTex = "No file to convert\\"

#Empty PNGs from output folder
for file in os.listdir(renamedOutput):
    if file.split(".")[1].lower() == "png":
        os.remove(os.path.join(renamedOutput, file))

doubleCheck = True
showTexturesNotInRexis = False
for arg in sys.argv:
    if arg == "--noDoubleCheck":
        doubleCheck = False
    if arg == "--showTexturesNotInRexis":
        showTexturesNotInRexis = True

for hashLookUp in lookUpTable:
    possableRexisTexture = os.path.join(RexisHashPath, hashLookUp.split(", ")[0] + ".png")
    if os.path.exists(possableRexisTexture):
        shutil.copy(possableRexisTexture, os.path.join(renamedOutput, hashLookUp.split(", ")[1]))
    else:
        #Double Check for file names that wern't found becase they have either a prefix or a suffix
        foundEqu = False
        if  doubleCheck:
            for RexisRoot, _Rexis, RexisFiles in os.walk(RexisHashPath):
                for RexisFile in RexisFiles:
                    hashFileName = RexisFile
                    hashPrefix = ""
                    if "-" in hashFileName:
                        hashFileName = hashFileName.split("-")[0]
                    if "_" in hashFileName:
                        hashPrefix, hashFileName = hashFileName.split("_")
                        hashPrefix = hashPrefix + "."
                    if ".png" in hashFileName:
                        hashFileName = hashFileName.split(".")[0]
                    if hashLookUp.split(", ")[0] == hashFileName:
                        print("Found", RexisFile, "during double check")
                        foundEqu = True
                        shutil.copy(os.path.join(RexisRoot, RexisFile), os.path.join(renamedOutput, hashLookUp.split(", ")[1].split(".")[0] + ".{}png".format(hashPrefix)))
        if (not foundEqu) and showTexturesNotInRexis:
            ##I'm not sure if I should remove this all together just yet
            #shutil.copy(os.path.join(root, file), missingTex)
            print("Rexis hash equivalent not found:", hashLookUp)
