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
   
def inputPlayerLetter():
      # Lets the player type which letter they want to be.
      # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':         
        return ['X', 'O']
      
    else:
        return ['O', 'X']
    
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
print ("") # spacing it out 
print("Welcome to Tic Tac Toe made by Kenji Mehl")
print ("") # spacing it out 
players = inputPlayerLetter()   
#makes a variable with first and second item in the players list
player = players[0]
computer = players[1]
      

while True:
    x = input("Select a spot: ")
    guess = int(x)
     
    if board[guess] != player and board[guess] != computer:
        board[guess] = player 
        if checkAll(player) == True:
            print("~~ X wins~~")
            break   

        while True: 
            opponent = random.randint(0,8)
            if board[opponent] != player and board[opponent] != computer:
                board[opponent] = computer
                boardp()
                if checkAll(computer) == True:
                    print ("~~O wins~~")
                    break
                break       
    else:
        print("This spot is taken")
                  
