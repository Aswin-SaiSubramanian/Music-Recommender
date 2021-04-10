import os
# Replace the path below with the path of id list
names_file = open('/home/matthew/Desktop/CPEN291_Final_Project_Repo/project-team-dilophosaurus/AssembleDataset_LatinElectronic/Latin')
names = set(line.rstrip('\n') for line in names_file.readlines())
names_file.close()
# Replace with path of MillionSongDataset (10000 Samples)
for root, dirs, files in os.walk('/home/matthew/Desktop/CPEN291_Final_Project_Repo/project-team-dilophosaurus/Latin Subset'):
    for name in files:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            name = name.replace(".h5","")
            if name not in names:
                os.remove(path)
