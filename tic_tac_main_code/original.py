import random
# The game board
board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
#board printer
def boardp():
    print (board[0],"|", board[1],"|", board[2])
    print ("---------")
    print (board[3],"|", board[4],"|", board[5])
    print ("---------")
    print (board[6],"|", board[7],"|", board[8])
   
def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
                return True

def checkAll(char):
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
print("Welcome to Tic Tac Toe made by Kenji Mehl")  

while True:
    x = input("Select a spot: ")
    guess = int(x)
     
    if board[guess] != "X" and board[guess] != "O":
        board[guess] = "X" 
        if checkAll("X") == True:
            print("~~ X wins~~")
            break   

        while True: 
            opponent = random.randint(0,8)
            if board[opponent] != "X" and board[opponent] != "O":
                board[opponent] = "O"
                boardp()
                if checkAll("O") == True:
                    print ("~~O wins~~")
                    break
                break       
    else:
        print("This spot is taken")
                  
