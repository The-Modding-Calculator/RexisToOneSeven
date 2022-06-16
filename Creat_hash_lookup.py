import xxhash
import numpy as np
import os
import sys
import shutil
from PIL import Image

if len(sys.argv) != 3:
    print("Usage: {} <input dir> <output look up table>".format(sys.argv[0]))
    sys.exit(0)

lookUpTable = []

xxh = xxhash.xxh32()
for root, _, files in os.walk(sys.argv[1]):
    for b in files:
        if os.path.splitext(b)[1] == '.png':
            p = os.path.join(root, b)
            im = np.array(Image.open(p).convert('RGBA'))
            mask = im[:, :, 3] > 0
            oldIM = im
            
            ##In the orginal script these would need to be used to unscale
            ##images to the PS2s alpha levels but we don't need them because
            ##mainline PCSX2 leaves the aplha untouched
            #im[:, :, 3][mask] >>= 1
            #im[:, :, 3][mask] += 1
            
            xxh.reset()
            xxh.update(np.ascontiguousarray(im))
            h = xxh.hexdigest()
            p2 = h.upper() + ", " + b
            if p2 in lookUpTable:
                print(f'"{p}" is duplicate of "{p2}"')
            else:
                print(f'"{p}" -> "{p2}"')
                lookUpTable.append(p2)

lookUpFileContence = ""
for entry in lookUpTable:
    lookUpFileContence = lookUpFileContence + entry + "\n"

lookUpFile = open(sys.argv[2], "w")
lookUpFile.write(lookUpFileContence)
lookUpFile.close()
