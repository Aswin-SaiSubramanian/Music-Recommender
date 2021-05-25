# Replace path below with MSD file containing all IDs and genres
# Download from http://www.ifs.tuwien.ac.at/mir/msd/download.html#groundtruth (MAGD Text File)
with open("Genres","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
	# Replace string below with the desired genre
        if "Latin" in line:
            f.write(line)
    f.truncate()
