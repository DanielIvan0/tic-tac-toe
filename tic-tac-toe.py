# Library
import random as rand

# Variables globales
players = ['', '']
currentPlayer = 0
board = [
    ['']*3,
    ['']*3,
    ['']*3
]

# Pedir jugadores
def getPlayers():
    exceptions = []
    while True:
        print('Ingrese los nombres de jugador (max 15 caracteres)')
        players[0] = input('Jugador 1: ')
        players[1] = input('Jugador 2: ')
        if players[0] == players[1]:
            exceptions.append('¡Ingresa nombres distintos!')
        if players[0] == '' or players[1] == '':
            exceptions.append('¡Ingresa un nombre no vacío!')
        if len(players[0]) > 15 or len(players[1]) > 15:
            exceptions.append('¡Ingresa un nombre más corto!')
        if len(exceptions) == 0:
            break
        else:
            for item in exceptions:
                print(item)
            exceptions.clear()

# Elegir el primer jugador
def chooseFirstPlayer():
    currentPlayer = rand.randint(0, 1)

# Mostrar el tablero
def showBoard():
    print('{:^3}|{:^3}|{:^3}'.format(board[0][0], board[0][1], board[0][2]))
    print('-----------')
    print('{:^3}|{:^3}|{:^3}'.format(board[1][0], board[1][1], board[1][2]))
    print('-----------')
    print('{:^3}|{:^3}|{:^3}'.format(board[2][0], board[2][1], board[2][2]))
# Manejador de turnos

# Ingresar jugada

# Evaluar tablero

# main function
def main():
    #getPlayers()
    showBoard()
    
main()