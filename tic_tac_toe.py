
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(symbol):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False


def start_game():
    global board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = "X"
    moves = 0

    while True:
        print_board()
        move = input(f"Player {turn}, choose a spot (1-9): ").strip()

        
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print(">> Invalid number! Enter 1-9.")
            continue

        pos = int(move) - 1

        if board[pos] in ['X', 'O']:
            print(">> Spot already taken! Pick another.")
            continue

       
        board[pos] = turn
        moves += 1

   
        if check_winner(turn):
            print_board()
            print(f"🎉 Player {turn} Wins! 🎉\n")
            break

       
        if moves == 9:
            print_board()
            print("🤝 It's a Draw! 🤝\n")
            break

        turn = "O" if turn == "X" else "X"

    again = input("Play again? (y/n): ").strip().lower()
    if again == 'y':
        start_game()
    else:
        print("Thanks for playing!")

start_game()