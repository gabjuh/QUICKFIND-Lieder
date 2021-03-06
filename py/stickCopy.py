def stickCopy():
    stick = input("Willst Du die Dateien auf einem Stick kopieren? (j/n)") 

    if stick == "j":
        print("Kopieren")
        return
    elif stick == "n":
        print("Danke für die Nutzung des Programms!")
        return
    else:
        print("Falsche angabe.")
        stickCopy()


  