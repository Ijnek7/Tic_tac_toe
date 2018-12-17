turnX = True
computer = False
import random
from tkinter import *
from tkinter import messagebox

root = Tk()
#title
root.title("Tic Tac Toe")
    
#example of computer 
# def turn(button, buttons):
#     global turnX
#     global computer
#     play = random.randint(0,8)
#     x = buttons[play]
#     if button["text"] == "" and turnX == True and computer == False:
#         button["text"] = "X" 
#         turnX = False
#     elif button["text"] == "" and turnX == False and computer == False:
#         button["text"] = "O" 
#         turnX = True
#     elif x["text"] == "" and turnX == False and computer == True:
#         x["text"] = "O"
#         turnX = True
#     elif button["text"] == "" and turnX == True and computer == True:
#         button["text"] = "X" 
#         turnX = False         
#     checkit()

def turn(button, buttons):
    global turnX
    global computer
    # play = random.randint(0,8)
    # x = buttons[play]
    if computer == False:
        if button["text"] == "" and turnX == True:
            button["text"] = "X"                                      
            turnX = False
        elif button["text"] == "" and turnX == False:
            button["text"] = "O" 
            turnX = True
    # elif computer == True:        
    #     while not x["text"] == "":
    #         play = random.randint(0,8)
    #         x = buttons[play]
    #     if x["text"] == "" and turnX == False:
    #             x["text"] = "O"
    #             turnX = True
    #     elif button["text"] == "" and turnX == True:
    #         button["text"] = "X" 
    #         turnX = False         
    checkit()
def single():
    if computer == True:        
        while not x["text"] == "":
            play = random.randint(0,8)
            x = buttons[play]
        if x["text"] == "" and turnX == False:
                x["text"] = "O"
                turnX = True
        elif button["text"] == "" and turnX == True:
            button["text"] = "X" 
            turnX = False          
    # if computer == True:
        # run computer placte thing function (take input of "x" or "o")

# def computer_turn():
#     play = random.randint(0,8)
#     x = buttons[play]
def checkit():
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button7["text"] == "X"and button8["text"] == "X"and button9["text"] == "X":
        messagebox.showinfo("Winner","!!!X has won!!!")
    elif button1["text"] == "O"and button2["text"] == "O"and button3["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button1["text"] == "O"and button4["text"] == "O" and button7["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button1["text"] == "O"and button5["text"] == "O" and button9["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button2["text"] == "O"and button5["text"] == "O" and button8["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button3["text"] == "O"and button6["text"] == "O"and button9["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button3["text"] == "O"and button5["text"] == "O"and button7["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button4["text"] == "O"and button5["text"] == "O"and button6["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")
    elif button7["text"] == "O"and button8["text"] == "O"and button9["text"] == "O":
        messagebox.showinfo("Winner","!!!O has won!!!")    
        
def reset():
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""

def computer_is_true():        
    global computer
    computer = True

# def computer(list_of_buttons, button):
#     global turnX
#     computer = random.randint(0,8)
#     x = list_of_buttons[computer]
#     if x["text"] == "" and turnX == False:
#         x["text"] == "O"
#         turnX == True 
# def Player():
#     button["text"] == "" and turnX == True:
#     button["text"] = "X" 
#     turnX = False

button = StringVar()
#black button with no text
button1 = Button(root, text = "", font = ("Times 30 bold"), bg = "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button1, buttons))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button2, buttons))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button3, buttons))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button4, buttons))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button5, buttons))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button6, buttons))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button7, buttons))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button8, buttons))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(root, text = "", font = ("Times 30 bold"), bg =  "grey", fg = "black", height = 5, width = 10, command = lambda:turn(button9, buttons))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

#makes a list of buttons
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

#making menu

dropdown = Menu(root)
root.config(menu = dropdown)
subMenu = Menu(dropdown)
dropdown.add_cascade(label = "Options", menu = subMenu)
subMenu.add_command(label= "Replay", command = reset)
subMenu.add_command(label = "Single Player Mode", command = computer_is_true)
# print(button1["text"])
# for i in buttons:
    # print(i["text"])
root.mainloop() 

