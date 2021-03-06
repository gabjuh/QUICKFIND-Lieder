def stickCopy():
    stick = input("Willst Du die Dateien auf einem Stick kopieren? (j/n)") 

    if stick == "j":
        print("Kopieren")
    elif stick == "n":
        print("Danke für die Nutzung des Programms!")
    else:
        print("Falsche angabe.")
        stickCopy()


stickCopy()