from distutils.dir_util import copy_tree
import os
import glob
import shutil
import array
# from py.stickCopy import *
from py.coloredInput import *
import winsound
import time



# Paths defined
targetPath = ".sermon_plan/"
sourcePath = "_Lieder_Paket_03.2021/"


printYellow('┌───────────────────────────────────────────────────────────────────────────────────────┐')
printYellow('|                                                                                       |')
printYellow('|                                        QUICKFIND                                      |')
printYellow('|                                   für Gemeindelieder                                  |')
printYellow('|                                                                                       |')
printYellow('|                               Entwickelt von Gábor Juhász                             |')
printYellow('|                                                                                       |')
printYellow('|                              © Gemeinde Bremen Mitte - 2021                           |')
printYellow('|                                                                                 v1.0  |')
printYellow('└───────────────────────────────────────────────────────────────────────────────────────┘\n\n')

printYellow("                Hallo,\n")
printYellow("                mit dem Tool kannst Du alle vorgegebene Lieder innerhalb")
printYellow("                von Sekunden finden und zusammensammeln, um Zeit und Arbeit")
printYellow("                zu sparen.\n")
printYellow("                Mehr dazu kannst unter Info (3) erfahren.\n")
printYellow("                Viel Spaß!\n\n")

printYellow("              > Quellenordner:     " + sourcePath)
printYellow("              > Zielordner:        " + targetPath + "\n\n")



promptText = "<QUICKFIND>"

def prompt(p=promptText):
    return analysis(colorInput(p + ': '))

def menu():
    printYellow("                       1) QUICKFIND starten\n")
    printYellow("                       2) Menü erneut abrufen\n")
    printYellow("                       3) Info\n")
    printYellow("                       x) Exit\n")
    prompt()
    # analysis(command)


def analysis(c):
    if c == "x":
        # Abschiedtext, countdown
        exit()
    elif c == "1":
        printYellow('┌───────────────────────────────────────────────────────────────────────────────────────┐')
        printYellow('|                                    Let\'s QUICKFIND!                                   |')
        printYellow('└───────────────────────────────────────────────────────────────────────────────────────┘')
    elif c == "2":
        menu()
        prompt()
    elif c == "3":
        printYellow("INFOTEXT FOLGT")
        prompt()
    else:
        printRed("Falsche Angabe, bitte noch einmal versuchen!")
        prompt()


menu()        





# Ask for Date and Fame for creating a folder

def setDatum():
    datum = colorInput('Datum von dem Predigt (TT.MM.JJJJ): ')
    checkDatum(datum)
    return datum

def checkDatum(d):
    errorMessage = "Bitte auf dem Format aufpassen: TT.MM.JJJJ, Beispiel: 01.01.2021"
    if len(d) != 10:
        printRed(errorMessage)
        setDatum() 
    elif d[2] != ".":
        printRed(errorMessage)
        setDatum() 
    elif d[5] != ".":
        printRed(errorMessage)
        setDatum() 
   

datum = str(setDatum())


name = colorInput('Name des Predigers: ')



# Creating Folder
path = targetPath + datum + " - " + name

try:
    os.mkdir(path)
except OSError:
    printRed ("Ordner wurde '%s' nicht angelegt." % path)
else:
    printGreen ("Ordner wurde erstellt '%s' ." % path)



# Get the numbers of Songs
nrOfSongs = colorInput("Anzahl von Lieder: ")



# Loop for each Song
for y in range(int(nrOfSongs)):


    # Finding Files
    files = []
    songNr = colorInput("Nummer des %s. Liedes (XXX): " % int(y + 1))

    # MP3
    mp3Matches = glob.glob(sourcePath + songNr + "*.mp3")
    # PPT/PPTX 
    pptxMatches = glob.glob(sourcePath + songNr + "*.ppt*")
    
        

    # Loop for printing found files
    printGreen("Folgende Dateien wurden gefunden:")
    for z in range(0, len(mp3Matches)):
        print(mp3Matches[z])



    # Loop for copying selected MP3 Files to the folder
    for b in range(len(mp3Matches)):
        fileName = mp3Matches[b].replace(sourcePath.replace("/","\\"), "")
        
        shutil.copyfile(mp3Matches[b], path + "/" + str(y + 1) + " - " + fileName)

        printGreen("Datei wurde kopiert: " + fileName + ",\nBefindet sich hier: " + path)
        


    # Loop for copying selected PPT/PPTX Files to the folder
    for b in range(len(pptxMatches)):
        fileName = pptxMatches[b].replace(sourcePath.replace("/","\\"), "")
        
        shutil.copyfile(pptxMatches[b], path + "/" + str(y + 1) + " - " + fileName)

        printGreen("Datei wurde kopiert: " + fileName + ",\nBefindet sich hier: " + path)
        



def stickCopy(fromDir, dirName):

    stick = colorInput("Willst Du die Dateien auf einem Stick kopieren? (j/n)") 
    
    if stick == "j":
        drive = colorInput("Aktueller Laufwerksbuchstabe: ")
        
        toDir = drive + ":/.temp/.agbm/_predigt_plaene/" + dirName
    
        copy_tree(fromDir, toDir)
        printGreen("Wurde erfolgreich kopiert.")
        printGreen("Danke für die Nutzung des Programms!")
        return
    elif stick == "n":
        printGreen("Danke für die Nutzung des Programms!")
        return
    else:
        printRed("Falsche angabe, manuelle Kopierung wird nötig. Bis zum nächsten Mal!")
        # stickCopy()



stickCopy(path, datum + " - " + name)


# Play Signal Tone if finished
filename = 'src/Alarm03.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)



# Countdown before closing
i = 5

def countdown_text():
    print("Das Fenster schließst sich in " + str(i) + " Sekunden.", end="\r" )

while i != 0:
    countdown_text()
    i -= 1
    time.sleep(1)
    countdown_text()



