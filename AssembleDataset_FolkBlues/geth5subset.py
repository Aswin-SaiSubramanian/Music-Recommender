# 1. Remove overlapping trackIDs
# 2. Remove trackIDs of wanted genre that are not in millionsongsubset
# 3. Get corresponding .h5 file in one folder so that it is easier to access

# untar millionsongsubset
import tarfile
fname = './millionsongsubset.tar.gz'
ap = tarfile.open(fname)
ap.extractall("C:/CPEN291/finalProject")
ap.close()

import os
# Replace the path below with the path of certain genre's id list
idFile = open('C:/CPEN291/finalProject/blues.txt')
trackIDs = set(line.rstrip('\n') for line in idFile.readlines())
idFile.close()

# file to store subset track ids
subset = open("C:/CPEN291/finalProject/bluesSubset.txt", "w")

# Replace with path of MillionSongDataset (10000 Samples)
for root, dirs, files in os.walk('C:/CPEN291/finalProject/MillionSongSubset'):
    for name in files:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            name = name.replace(".h5","")
            if name not in trackIDs:
                os.remove(path)
            else:
                subset.write(name)
                subset.write("\n")
subset.close()

import shutil
for root, dirs, files in os.walk('C:/CPEN291/finalProject/MillionSongSubset'):
    # move .h5 files to one folder
    des = 'C:/CPEN291/finalProject/blues/'
    for name in files:
        path = os.path.join(root, name)
        shutil.move(path, des + name)
