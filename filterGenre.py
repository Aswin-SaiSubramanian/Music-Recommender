# trackIDs get from "http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-MAGD-genreAssignment.cls"

file = open("C:/CPEN291/finalProject/trackIDs.txt", "r")
folk = open("C:/CPEN291/finalProject/folk.txt", "w")
blues = open("C:/CPEN291/finalProject/blues.txt", "w")


while True:
    line = file.readline()
    if not line:
        break
    else:
        songInfo = line.rstrip().split("	")
        genre = songInfo[-1]
        trackID = songInfo[0]
        if genre == "Folk":
            folk.write(trackID)
            folk.write("\n")
        elif genre == "Blues":
            blues.write(trackID)
            blues.write("\n")
            
file.close()
folk.close()
blues.close()      
        
