import os
import sys
import shutil

if not (len(sys.argv) > 3):
    print("Usage: renxxh.py <multi hash textures dir> <Rexis Upscaled Textures dir> <output dir>")
    sys.exit(0)

modernHashPath = sys.argv[1]
RexisHashPath = sys.argv[2]

renamedOutput = sys.argv[3]

missingTex = "No file to convert\\"

doubleCheck = True
if sys.argv > 4:
    if sys.argv[4] == "--noDoubleCheck":
        doubleCheck = False

for root, _, files in os.walk(modernHashPath):
    for file in files:
        OneSevenTexInRexisPath = os.path.join(RexisHashPath, file.split("_")[0] + ".png")
        if os.path.exists(OneSevenTexInRexisPath):
            shutil.copy(OneSevenTexInRexisPath, os.path.join(renamedOutput, file.split("_")[1]))
        else:
            #Double Check for file names that wern't found becase they have either a prefix or a suffix
            foundEqu = False
            if  doubleCheck:
                for RexisRoot, _Rexis, RexisFiles in os.walk(RexisHashPath):
                    for RexisFile in RexisFiles:
                        if file.split("_")[0] in RexisFile:
                            print("Found", RexisFile, "during double check")
                            foundEqu = True
                            shutil.copy(os.path.join(RexisRoot, RexisFile), os.path.join(renamedOutput, file.split("_")[1]))
            if not foundEqu:
                shutil.copy(os.path.join(root, file), missingTex)
                print("Rexis hash equivalent not found:", file)
