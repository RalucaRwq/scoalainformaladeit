# create empty board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_not_end = True
print("Let's play a  game! You are first.")
global last_move
last_move = "initial"
global is_tie
is_tie = False

def check_win():
    global game_not_end
    if board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-"\
            or board[6] == board[7] == board[8] != "-":  # check rows
        game_not_end = False
    elif board[0] == board[3] == board[6] != "-" or board[1] == board[4] == board[7] != "-" \
            or board[2] == board[5] == board[8] != "-":  # check column
        game_not_end = False
    elif board[0] == board[4] == board[8] != "-" or board[2] == board[4] == board[6] != "-":
        game_not_end = False  # check diagonals


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")


display_board()

while game_not_end:
    if "-" in board:
        user_input = input("Please choose a position from 1-9: ")
        if user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            continue
        else:
            get_index = int(user_input) - 1
            if board[get_index] == "-":  # check if this place is empty
                board[get_index] = "X"
                last_move = "X"
                check_win()
                if not game_not_end:
                    display_board()
                    break
                if board[4] == "-":  # check if the user chose position 5
                    board[4] = "O"
                    last_move = "O"
                    display_board()
                elif board[0] == "-" or board[2] == "-" or board[6] == "-" or board[8] == "-":
                    good_positions = [0, 2, 6, 8, 1, 3, 5, 7]
                    for i in good_positions:
                        if board[i] == "-":
                            board[i] = "O"
                            last_move = "O"
                            display_board()
                            check_win()
                            break
            else:
                print("This position is already occupied.")
                display_board()
                continue
    else:
        display_board()
        print("IT'S A TIE!")
        is_tie = True
        break

if is_tie is False:
    if last_move == "O":
        print("YOU LOST!")
    else:
        print("YOU WON!")


