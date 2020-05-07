# Library
import random as rand

# Variables globales
players = ['', '']
symbols = ['X', 'O']
currentPlayer = 0
moves = ('1', '2', '3')
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
        insertPlay()
        showBoard()
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
    while True:
        i = input(f'{players[currentPlayer]}, inserte la fila de su jugada: ')
        j = input(f'{players[currentPlayer]}, inserte la columna de su jugada: ')
        if i not in moves or j not in moves:
            print('¡Movimiento inválido!')
        elif board[int(i) - 1][int(j) - 1] in symbols:
            print('¡Casilla ocupada!')
        else:
            board[int(i) - 1][int(j) - 1] = symbols[currentPlayer]
            break

# Evaluar tablero
def youWon():
    if rowDetected() or diagonalDetected() or columnDetected():
        return True
    return False
def rowDetected():
    if [symbols[currentPlayer]]*3 in board:
        return True
    return False
def diagonalDetected():
    principal = [board[i][i] for i in range(len(board))]
    secondary = [board[(len(board) - 1) - i][i] for i in range(len(board))]
    if principal == [symbols[currentPlayer]]*3 or secondary == [symbols[currentPlayer]]*3:
        return True
    return False
def columnDetected():
    if [symbols[currentPlayer]]*3 in [[board[j][i] for j in range(len(board[i]))] for i in range(len(board))]:
        return True
    return False

def fullBoard():
    for row in board:
        for item in row:
            if len(item) == 0:
                return False
    else:
        return True

# main function
def main():
    getPlayers()
    chooseFirstPlayer()
    showBoard()
    start()
    
main()