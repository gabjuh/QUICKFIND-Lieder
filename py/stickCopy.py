from distutils.dir_util import copy_tree
import shutil

def stickCopy(fromDir, dirName):

    stick = input("Willst Du die Dateien auf einem Stick kopieren? (j/n)") 
    
    if stick == "j":
        drive = input("Aktueller Laufwerksbuchstabe: ")
        
        toDir = drive + ":/.temp/.agbm/_predigt_plaene/" + dirName
    
        copy_tree(fromDir, toDir)
        print("Wurde erfolgreich kopiert.")
        print("Danke für die Nutzung des Programms!")
        return
    elif stick == "n":
        print("Danke für die Nutzung des Programms!")
        return
    else:
        print("Falsche angabe, manuelle Kopierung wird nötig. Bis zum nächstes Mal!")
        # stickCopy()


# k:\.temp\.agbm\_predigt_plaene\