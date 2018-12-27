from tkinter import Tk, messagebox, Button, Menu, S,N,E,W
import time, random

turnX = True
computer = False
p1, p2, e = "X", "O", ""

root = Tk()
root.title("Tic Tac Toe")

def turn(button, buttons):
    global turnX
    global computer
    if button["text"] == e:
        if computer == False:
            multi(button, buttons)
        if computer == True: 
            single(button, buttons)

def multi(button, buttons):
    global turnX
    if turnX == True:
        button["text"] = "X"                                      
        turnX = False
    elif turnX == False:
        button["text"] = "O" 
        turnX = True
    checkit(button)

def single(button, buttons):
    button["text"] = p1
    
    result = checkVictory(button)
    if result == p1:
        messagebox.showinfo("Game Over",result+" has won the game!")
        reset()
        return
    if result == "Tie":
        messagebox.showinfo("Game Over","This game was a tie!")
        reset()
        return

    time.sleep(0.25)
    
    randx, randy = random.randint(0,2), random.randint(0,2)
    while not buttons[randx][randy]["text"] == e:
        randx = random.randint(0,2)
        randy = random.randint(0,2)
    if buttons[randx][randy]["text"] == e:
        buttons[randx][randy]["text"] = p2

    checkit(buttons[randx][randy])

def getlayout():
    convertedList = [[e,e,e],[e,e,e],[e,e,e]]
    for i in range(0,3):
        for j in range(0,3):
            convertedList[i][j] = buttons[i][j]["text"]
    return convertedList

def checkVictory(button):
    x , y = int(button.grid_info()['column']), int(button.grid_info()['row'])
    board = getlayout()

    if board[0][x] == board[1][x] == board [2][x]: # vertical win
        return board[y][x]

    if board[y][0] == board[y][1] == board [y][2]: # horizontal win
        return board[y][x]

    if y == x and board[0][0] == board[1][1] == board [2][2]: # diagonal win case 1
        return board[y][x]

    if y + x == 2 and board[0][2] == board[1][1] == board [2][0]: # diagonal win case 2
        return board[y][x]

    turnString = e
    for i in range(len(board)):
        for j in range(len(board[i])):
            turnString+=board[i][j]
    turn = len(turnString)    
    if turn >= 9:
        return "Tie"
    
    return False

def checkit(button): # TODO: Merge this function with the checkVictory function
    result = checkVictory(button)
    if result == "Tie":
        messagebox.showinfo("Game Over","This game was a tie!")
        reset()
        
    elif result==p1 or result==p2:
        messagebox.showinfo("Game Over",result+" has won the game!")
        reset()
        
def reset():
    reset_board = [[e,e,e],[e,e,e],[e,e,e]]
    for i in range(len(reset_board)):
        for j in range(len(reset_board[i])):
            buttons[i][j]["text"] = reset_board[i][j]

def computer_is_true():        
    global computer
    reset()
    computer = True
# TODO: don't have small dedicated functions 
def computer_is_false():        
    global computer
    reset()
    computer = False

def start():
    global buttons
    buttons = []
    for i in range(0,3):
        temp_buttons = []
        for j in range(0,3):
            b = Button(root, text = e, font = ("Times 30 bold"), bg = "grey", fg = "black", height = 5, width = 10) 
            action = lambda x = b: turn(x, buttons)
            b.configure(command = action)
            temp_buttons.append(b)
            temp_buttons[j].grid(row=i, column=j, sticky = S+N+E+W)
        buttons+=[temp_buttons]

start()
dropdown = Menu(root)
root.config(menu = dropdown)
subMenu = Menu(dropdown)
dropdown.add_cascade(label = "Options", menu = subMenu)
subMenu.add_command(label= "Replay", command = reset)
subMenu.add_command(label = "Single player Mode", command = computer_is_true)
subMenu.add_command(label = "Multi player Mode", command = computer_is_false)

root.mainloop()