 #tic_tac_toe
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

sign_dictionary = []#se hace un arreglo 
for i in range (9):#Cantidad de celdas que se le asignaran al arreglo
    sign_dictionary.append(' ')#se añade un espacio en blanco a la lista "sign_dictionary"

def print_board():
    board = f"""

    {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
   ---|---|---
    {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
   ---|---|---
    {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}


   """
    print(board)

index_list = []
def take_input(player_name):
    while True:
        x = int(input(f"{player_name}: "))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print("Ya esta ocupada")
                continue 
            index_list.append(x)
            return x
         print("Ingresa un numero entre 1-9")        
    
def main():
    print("Welcome to tic tac toe game.!")
    player_one = input("Enter player one name: ")#almacena el nombre del jugador en player_one
    player_two = input("Enter player two name: ")#almacena el nombre del jugador en player_two
    print(f"Thank you for joining {player_one} and {player_two}")#cadena de formato "f"

    print(instrucciones)
    print(f"{player_one} sera X")
    print(f"{player_two} sera O")
    input("Digite cualquier letra o numero para comenzar el juego: ")

    print_board()

    for i in range(9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dictionary[index] = 'X'
         else:
            index = take_input(player_two)
            sign sign_dictionary[index] = "O"


main()
