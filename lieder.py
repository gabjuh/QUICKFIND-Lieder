import os
import glob
import shutil
import array
from py.stickCopy import *


# Paths defined
plansPath = ".sermon_plan/"
songsPath = "_Lieder_Paket_03.2021/"



# Ask for Date and Fame for creating a folder
datum = input("Datum: (JJJJ.MM.TT) ")
name = input("Name des Predigers: ")



# Creating Folder
path = plansPath + datum + " - " + name

try:
    os.mkdir(path)
except OSError:
    print ("Ordner wurde '%s' nicht angelegt." % path)
else:
    print ("Ordner wurde erstellt '%s' ." % path)



# Get the numbers of Songs
nrOfSongs = input("Anzahl von Lieder: ")



# Loop for each Song
for y in range(int(nrOfSongs)):


    # Finding Files
    files = []
    songNr = input("Nummer des %s. Liedes (XXX): " % int(y + 1))

    # MP3
    mp3Matches = glob.glob(songsPath + songNr + "*.mp3")
    # PPT/PPTX 
    pptxMatches = glob.glob(songsPath + songNr + "*.ppt*")
    
        

    # Loop for printing found files
    print("Folgende Dateien wurden gefunden:")
    for z in range(0, len(mp3Matches)):
        print(mp3Matches[z])



    # Loop for copying selected MP3 Files to the folder
    for b in range(len(mp3Matches)):
        fileName = mp3Matches[b].replace(songsPath.replace("/","\\"), "")
        
        shutil.copyfile(mp3Matches[b], path + "/" + str(y + 1) + " - " + fileName)

        print("Datei wurde kopiert: " + fileName + ",\nBefindet sich hier: " + path)
        


    # Loop for copying selected PPT/PPTX Files to the folder
    for b in range(len(pptxMatches)):
        fileName = pptxMatches[b].replace(songsPath.replace("/","\\"), "")
        
        shutil.copyfile(pptxMatches[b], path + "/" + str(y + 1) + " - " + fileName)

        print("Datei wurde kopiert: " + fileName + ",\nBefindet sich hier: " + path)
        



stickCopy()


