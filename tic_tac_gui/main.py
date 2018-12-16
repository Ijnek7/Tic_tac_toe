from tkinter import *
root = Tk()
turnX = True
def turn(button):
    if button["text"] == "" and turnX == True:
        button["text"] = "X" 
        turnX = False
    elif button["text"] == "" and turnX == False:
        button["text"] = "O" 
        turnX = True


def checker():
    
    
    if checkLine(char, 0, 1, 2):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True

root.mainloop()        