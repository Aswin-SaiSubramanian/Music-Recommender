# trackIDs get from "http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-MAGD-genreAssignment.cls"
file = open("C:/CPEN291/finalProject/trackIDs.txt", "r")

# open files to write filtered track ids
folk = open("C:/CPEN291/finalProject/folk.txt", "w")
blues = open("C:/CPEN291/finalProject/blues.txt", "w")

# iterate through file line by line
while True:
    line = file.readline()
    
    # when there is no more line to read, stop iteration
    if not line:
        break
    
    # based on the wanted genre copy the trackID to separate files
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

# close files when done
file.close()
folk.close()
blues.close()      
        
