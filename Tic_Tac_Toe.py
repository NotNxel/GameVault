# GameVault: Tic-Tac-Toe
# A classic 3x3 grid game made by Neel, Monish, and Reyansh.
# Welcome to GameVault! This collection includes a variety of mini-games like Tic-Tac-Toe, 
# 2048, Tetris, and JoJo-inspired challenges. Enjoy the fun and test your skills across 
# different game modes.
# GitHub Repository: https://github.com/NotNxel/GameVault
# © 2025 Neel , Reyansh And Monish. All rights reserved.

import random

# Game Design
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWin(board, player):
    win_combinations = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L']
    ]
    
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def checkDraw(board):
    for key in board:
        if board[key] == ' ':
            return False
    return True

def playerMove(board, player):
    while True:
        move = input(f"Player {player}, choose a position (top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R): ")
        if move in board and board[move] == ' ':
            board[move] = player
            break
        else:
            print("Invalid move. Try again.")

def botMove(board):
    available_moves = [key for key, value in board.items() if value == ' ']
    move = random.choice(available_moves)
    print(f"Bot chooses {move}")
    board[move] = 'O'

def playGame():
    print("Welcome to **GameVault**!")
    print("Enjoy a variety of mini-games including Tic-Tac-Toe, 2048, Tetris, and JoJo-inspired challenges.")
    print("Made by Neel, Monish, and Reyansh.")
    
    mode = input("Choose game mode: 1 - Player vs Player, 2 - Player vs Bot: ")
    
    if mode == '1':
        player = 'X'
        while True:
            printBoard(theBoard)
            playerMove(theBoard, player)
            if checkWin(theBoard, player):
                printBoard(theBoard)
                print(f"Player {player} wins!")
                break
            elif checkDraw(theBoard):
                printBoard(theBoard)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
    elif mode == '2':
        player = 'X'
        while True:
            printBoard(theBoard)
            if player == 'X':
                playerMove(theBoard, player)
            else:
                botMove(theBoard)
            
            if checkWin(theBoard, player):
                printBoard(theBoard)
                if player == 'X':
                    print("Player X wins!")
                else:
                    print("Bot wins!")
                break
            elif checkDraw(theBoard):
                printBoard(theBoard)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'

playGame()
