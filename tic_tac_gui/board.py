from tkinter import *

root = Tk()
#title
root.title("Tic Tac Toe")

turnX = True

def turn(button):
    if button["text"] == "" and turnX == True:
        button["text"] = "X" 
        turnX = False
    elif button["text"] == "" and turnX == False:
        button["text"] = "O" 
        turnX = True

button = StringVar()
#black button with no text
button1 = Button(root, text = " ", font = ("Times 20 bold"), bg = "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button4))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button6))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button7))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button8))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(root, text = " ", font = ("Times 20 bold"), bg =  "grey", fg = "green", height = 5, width = 10, command = lambda:turn(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

root.mainloop() 