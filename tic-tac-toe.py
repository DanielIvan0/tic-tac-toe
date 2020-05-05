# Library
import random as rand

# Variables globales
players = ['', '']
symbols = ['X', 'O']
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
    global currentPlayer
    currentPlayer = rand.randint(0, 1)
    print(f'El primer jugador es {players[currentPlayer]}')

# Iniciar el juego
def start():
    while True:
        showBoard()
        insertPlay()
        if youWon():
            print('Tú ganaste')
            break
        if fullBoard():
            print('Tablero está lleno')
            break
        changePlayer()

# Mostrar el tablero
def showBoard():
    print('{:^3}|{:^3}|{:^3}'.format(board[0][0], board[0][1], board[0][2]))
    print('-----------')
    print('{:^3}|{:^3}|{:^3}'.format(board[1][0], board[1][1], board[1][2]))
    print('-----------')
    print('{:^3}|{:^3}|{:^3}'.format(board[2][0], board[2][1], board[2][2]))

# Manejador de turnos
def changePlayer():
    global currentPlayer
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0

# Ingresar jugada
def insertPlay():
    play = input(f'{players[currentPlayer]}, inserte su jugada: ')
    if len(play) == 2:
        if play[0] in ('1', '2', '3') and play[1] in ('1', '2', '3'):
            pass
        else:
            pass
    else:
        pass

# Evaluar tablero
def youWon():
    # Retorna True si el jugador actual gana
    # Retorna False en caso contrario
    pass

def fullBoard():
    # Retorna True si el tablero está vacío
    # Retorna False en caso contrario
    pass

# main function
def main():
    getPlayers()
    chooseFirstPlayer()
    start()
    
main()