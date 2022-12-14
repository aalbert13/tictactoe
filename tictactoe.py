board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

current_player = "X"
winner = None
gameRunning = True 



def display_board(board): 
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8]) 
   


# player input
def player_input(board):
    inp = int(input("Enter number 1-9: "))
    if inp >=1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Spot already played!")    


# check win condition
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "=":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "=":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "=":
        winner = board[6]
        return True


def check_rows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "=":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "=":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "=":
        winner = board[2]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "=":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "=":
        winner = board[2]
        return True


def check_tie(board):
    global gameRunning
    if "-" not in board:
        display_board(board)
        print("It is a tie!")
        gameRunning = False

def check_win():
    if check_horizontal(board) or check_horizontal(board) or check_rows(board):
        print(f"Winner is {winner}")         


#switch player
def switch_player():
    global current_player
    if current_player =="X":
        current_player = "O"
    else:
        current_player = "X"                 


while gameRunning:
    display_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()

