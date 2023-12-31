# print("suuuuuuuh")
import random

board = ["-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-",]

# board = ["1 ", "2 ", "3 ", "4 ", "5 ",
#          "6 ", "7 ", "8 ", "9 ", "10 ",
#          "11", "12", "13", "14", "15",
#          "16", "17", "18", "19", "20",
#          "21", "22", "23", "24", "25",
#          "26", "27", "28", "29", "0",]

#5X6

currentPlayer = "X"
winner = None
gameRunning = True

# takes in board argument


def printBoard(board):
    print("Ticky Tacky Toesy")
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4])
    print("-------------------")
    print(board[5] + " | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9])
    print("-------------------")
    print(board[10] + " | " + board[11] + " | " + board[12] + " | " + board[13] + " | " + board[14])
    print("-------------------")
    print(board[15] + " | " + board[16] + " | " + board[17] + " | " + board[18] + " | " + board[19])
    print("-------------------")
    print(board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23] + " | " + board[24])
    print("-------------------")
    print(board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28] + " | " + board[29])
    print("-------------------")



printBoard(board)

# take player input
#FOR SOME REASON, '0' IS GETTING READ AS '30' IN PYTON DEBUGGER

def playerInput(board):
    inp = int(input("Enter Sandman 0-29: "))
    if inp >= 0 and inp <= 29 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Getcho own square!!")

# check for win/tie
    # tapping into global variable winner
    # global keyord means that if winner changes within this function, it affects the entire file
    # if any change is applied to winner, the scope of it applies to the whole file


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] == board[3] == board[4] and board[0] != "-":
        winner = board[0]
        return True
    elif board[5] == board[6] == board[7] == board[8] == board[9] and board[5] != "-":
        winner = board[3]
        return True
    elif board[10] == board[11] == board[12] == board[13] == board[14] and board[10] != "-":
        winner = board[6]
        return True
    elif board[15] == board[16] == board[17] == board[18] == board[19] and board[15] != "-":
        winner = board[6]
        return True
    elif board[20] == board[21] == board[22] == board[23] == board[24] and board[20] != "-":
        winner = board[6]
        return True
    elif board[25] == board[26] == board[27] == board[28] == board[29] and board[25] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[5] == board[10] == board[15] == board[20] == board[25] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[6] == board[11] == board[16] == board[21] == board[26] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[7] == board[12] == board[17]== board[22] == board[27] and board[2] != "-":
        winner = board[2]
        return True
    if board[3] == board[8] == board[13] == board[18]== board[23] == board[28] and board[3] != "-":
        winner = board[3]
        return True
    if board[4] == board[9] == board[14] == board[19]== board[24] == board[29] and board[4] != "-":
        winner = board[4]
        return True


def checkDiag(board):
    global winner
    if board[1] == board[7] == board[13] == board[19] == board[25] and board[1] != "-":
        winner = board[1]
        return True
    if board[6] == board[12] == board[18] == board[24] == board[0] and board[6] != "-":
        winner = board[6]
        return True
    if board[5] == board[9] == board[13] == board[17] == board[21] and board[5] != "-":
        winner = board[5]
        return True
    if board[10] == board[14] == board[18] == board[22] == board[26] and board[10] != "-":
        winner = board[10]
        return True
    
# 1,7,13,19,25
# 6,12,18,24,0
# 5,9,13,17,21
# 10,14,18,22,26


def checkTie(board):
    global gameRunning
    if "-" not in board:
        print("DRAW")
        gameRunning = False


def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkDiag(board):
        print(f"The winner is {winner}")
# def checkWin():
#     if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
#         print(f"The winner is {winner}")

# switch player


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 29)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# check for win/tie again


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
