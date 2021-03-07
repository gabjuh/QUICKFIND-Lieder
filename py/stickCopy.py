from distutils.dir_util import copy_tree
import shutil
import coloredInput as ci


def stickCopy(fromDir, dirName):

    stick = ci.colorInput("Willst Du die Dateien auf einem Stick kopieren? (j/n)") 
    
    if stick == "j":
        drive = ci.colorInput("Aktueller Laufwerksbuchstabe: ")
        
        toDir = drive + ":/.temp/.agbm/_predigt_plaene/" + dirName
    
        copy_tree(fromDir, toDir)
        ci.printGreen("Wurde erfolgreich kopiert.")
        ci.printGreen("Danke für die Nutzung des Programms!")
        return
    elif stick == "n":
        ci.printGreen("Danke für die Nutzung des Programms!")
        return
    else:
        ci.printRed("Falsche angabe, manuelle Kopierung wird nötig. Bis zum nächsten Mal!")
        # stickCopy()


# k:\.temp\.agbm\_predigt_plaene\