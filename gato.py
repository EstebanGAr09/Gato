# tic_tac_toe
""""
[x]:Draw a board
[x]:Input player name
[]:Put a sign to each player
[]: if user doesn't input between(1-9), direct them to previous state
[]: Put sign to exact spot after taking user input
[]:Print board after each input
[]:Calculate and display the result
"""

instrucciones = """
Este sera el tablero del gato

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

 Instrucciones: 
 1 Digita un numero entre (1-9) para poner tu signo
 2 Deberan llenarse todas las casillas para obtener el resultado
 3 El jugador 1 siempre empezara primero 
 """




def correct_input(x):
    if (x.isnumeric()):
        if (0 < int(x) < 10):
            return True
    return False


def print_board(board):

    b="""-{0}- | -{1}- | -{2}-
_____
-{3}- | -{4}- | -{5}-
_____
-{6}- | -{7}- | -{8}-"""
    print(b.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],))

    """row1 = board[0]," | ",board[1], "|" ,board[2]
    row2=board[3]," | ",board[4], "|" ,board[5]
    row3=board[6]," | ",board[7], "|" ,board[8]


   # print(b.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))
    print(row1)
    print("__________")
    print(row2)
    print("_________")
    print(row3)"""





def check_winner(board):
    # Se checka el ganador horizonatal
    if (board[0] == board[1] and board[1] == board[2]):
        return  board[0]
    if (board[3] == board[4] and board[4] == board[5]):
        return board[3]
    if (board[6] == board[7] and board[7] == board[8]):
        return board[6]

    # Se checka vertical
    if (board[0] == board[3] and board[3] == board[6]):
        return board[0]
    if (board[1] == board[4] and board[4] == board[7]):
        return board[1]
    if (board[2] == board[5] and board[5] == board[8]):
        return board[2]
    # se checka vertical
    if (board[0] == board[4] and board[4] == board[8]):
        return board[0]
    if (board[2] == board[4] and board[4] == board[6]):
        return board[2]
    return False


def is_tie(board):
    count = 0
    for x in range(0, 9):
        if (board[x] == "x" or board[x] == "o"):
            count = count+1
        else:
            return False
    if (count == 9):
        return True
    return False


def is_position_available(board,pas):
    if (board [pas] == "x" ):
        return False
    if (board [pas] == "o"):
        return False
    return True




def take_input(player_name):
    x = int(input(f"{player_name}: "))
    if (correct_input(x) == True):
        return x
    return -1


def main():

    i = 0
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("Welcome to tic tac toe game.!")
    player_one = input("Enter player one name: ")  # almacena el nombre del jugador en player_one
    player_two = input("Enter player two name: ")  # almacena el nombre del jugador en player_two
    print(f"Thank you for joining {player_one} and {player_two}")  # cadena de formato "f"
    """
    la "f" antes de las comillas indica que es una cadena de formato, y las expresiones entre las llaves 
    ("{}")son reemplazadas por sus valores correspondientes
    """

    print(print_board(board))
    while (True):
        if i % 2 == 0:

            print("Choose a position", player_one)
        else:
            print("Choose a position ", player_two)

        index = input("enter a position ")
        if (correct_input(index) == True and is_position_available(board, int(index)-1)):
            if i % 2 == 0:
                board[int(index) - 1] = 'o'
            else:
                board[int(index) - 1] = "x"
        else:
            print("Invalid position, Try again :( ")
        i = i + 1
        winner=check_winner(board)
        if(winner=="o" or winner=="x"):
            if(winner=="o"):
                print("Congratulations, you're the winner",player_one)
            else:
                print("Congratulations", player_two)

            break
        elif(is_tie(board)==True):
            print("it is a tie!")
            break
        print_board(board)








main()