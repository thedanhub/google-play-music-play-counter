import os
import csv

# Enter the path to Google Play Music takeout folder, Tracks subfolder
export_folder = '/Users/username/Downloads/Takeout/Google Play Music/Tracks'

# Calculate how many songs to include in the list
numberoffiles = 0
for root, dirs, files in os.walk(export_folder):
    for file in files:
        if file.endswith((".csv")):
            numberoffiles = numberoffiles + 1

# Prepare an empty Matrix with title and play count columns
rows, cols = 4, numberoffiles
Matrix = [[0 for x in range(rows)] for y in range(cols)]
counter = -1

# Fetch title and play count info from each CSV file
# Enter it into the Matrix
for root, dirs, files in os.walk(export_folder):
    for (idx,name) in enumerate(files):
        if name.endswith((".csv")):
            counter = counter + 1
            file = os.path.join(root, name)
            with open(file, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(spamreader)
                for row in spamreader:
                    try:
                        Matrix[counter][0] = row[0] # title
                        Matrix[counter][1] = row[2] # artist
                        Matrix[counter][2] = int(row[5]) # count
                        Matrix[counter][3] = row[1] # album
                    except:
                        print('Missing attribute')

# Sort the matrix with most listened to tracks first
for idx, row in enumerate(sorted(Matrix, key=lambda x: x[2], reverse=True)):
    print("[" + str(idx+1) + "] " + str(row[2]) + " - " + str(row[0]) + ", " + str(row[1]) + " [" + str(row[3]) + "]")