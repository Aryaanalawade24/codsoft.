# Unbeatable Tic-Tac-Toe using Minimax Algorithm

import math

HUMAN = "X"
AI = "O"
EMPTY = " "

board = [EMPTY for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---------")
    print()

def is_winner(player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_draw():
    return EMPTY not in board

def minimax(is_maximizing):
    if is_winner(AI):
        return 1
    if is_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    board[move] = AI

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == EMPTY:
                board[move] = HUMAN
                break
            else:
                print("Position already taken.")
        except:
            print("Invalid input. Enter number between 1-9.")

def main():
    print("TIC-TAC-TOE (You vs AI)")
    print("You are X | AI is O")
    print_board()

    while True:
        human_move()
        print_board()

        if is_winner(HUMAN):
            print("🎉 You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print("AI played:")
        print_board()

        if is_winner(AI):
            print("🤖 AI wins! Unbeatable 😎")
            break
        if is_draw():
            print("It's a draw!")
            break

main()
