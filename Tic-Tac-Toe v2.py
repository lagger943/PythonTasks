import os
import random


class TicTacToe:
    def __init__(self):
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.player_pts = 0
        self.comp_pts = 0

    def print_board(self):
        print(f" Your wins: {self.player_pts} | Computer Wins: {self.comp_pts}")
        print(f"   ┌───┬───┬───┐\n   │ {self.game_board[6]} │ {self.game_board[7]} │ {self.game_board[8]}"
              f" │\n   │───┼───┼───┤\n   │ {self.game_board[3]} │ {self.game_board[4]} │ {self.game_board[5]}"
              f" │\n   ├───┼───┼───┤\n   │ {self.game_board[0]} │ {self.game_board[1]} │ {self.game_board[2]}"
              f" │\n   └───┴───┴───┘\n", end='')

    def add_player_pts(self):
        self.player_pts = self.player_pts + 1

    def add_comp_pts(self):
        self.comp_pts = self.comp_pts + 1

    def check_validity(self, selection):
        if (selection not in range(0, 9)
                or self.game_board[selection] != ' '):
            return False
        else:
            return True

    def make_turn(self, selection, player):
        if player == 1:
            self.game_board[selection] = 'X'
        else:
            self.game_board[selection] = '0'

    def check_for_win(self, player):
        if (self.game_board[6] == self.game_board[7] == self.game_board[8] != ' '
                or self.game_board[3] == self.game_board[4] == self.game_board[5] != ' '
                or self.game_board[0] == self.game_board[1] == self.game_board[2] != ' '
                or self.game_board[8] == self.game_board[5] == self.game_board[2] != ' '
                or self.game_board[7] == self.game_board[4] == self.game_board[1] != ' '
                or self.game_board[6] == self.game_board[3] == self.game_board[0] != ' '
                or self.game_board[0] == self.game_board[4] == self.game_board[8] != ' '
                or self.game_board[6] == self.game_board[4] == self.game_board[2] != ' '):
            if player == 1:
                self.add_player_pts()
            else:
                self.add_comp_pts()
            return True
        else:
            return False

    def check_full_board(self):
            if ' ' not in self.game_board:
                return True
            else:
                return False

    def clear_board(self):
        for i in range(len(self.game_board)):
            self.game_board[i] = ' '


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear_board')


def start():
    print("\n")
    print("\t\t\t\t▓▓▓▓▓ ▓ ▓▓▓▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓"
          "\n\t\t\t\t  ▓     ▓        ▓    ▓ ▓  ▓         ▓   ▓   ▓ ▓    "
          "\n\t\t\t\t  ▓   ▓ ▓    ▓   ▓   ▓   ▓ ▓     ▓   ▓   ▓   ▓ ▓▓▓▓▓"
          "\n\t\t\t\t  ▓   ▓ ▓        ▓   ▓▓▓▓▓ ▓         ▓   ▓   ▓ ▓    "
          "\n\t\t\t\t  ▓   ▓ ▓▓▓▓     ▓   ▓   ▓ ▓▓▓▓▓     ▓   ▓▓▓▓▓ ▓▓▓▓▓\n")
    print("\n How to play:\n You play this game with numpad of the keyboard. "
          "Number placement corresponds to the columns in the game. Example:\n", end='')
    print("   ┌───┬───┬───┐\n   │ 7 │ 8 │ 9 │\n   │───┼───┼───┤\n   │ 4 │ 5 │ 6 │"
          "\n   ├───┼───┼───┤\n   │ 1 │ 2 │ 3 │\n   └───┴───┴───┘\n", end='')
    os.system("pause")


def game():
    clear()
    if random.randint(1, 20) > 10:  #Ysed to pick at random who will be first
        player = 1
    else:
        player = 2
    full_board = False
    while full_board is False:
        good_selection = False  #Variable for selection check result
        while good_selection is False:  #Promt for selection until it's right
            if player == 1:
                clear()
                x.print_board()
                p_input = input(" Enter your choice:")
                try:
                    int(p_input)
                except ValueError:
                    clear()
                    continue
                selection = int(p_input) - 1
                good_selection = x.check_validity(selection)
            else:
                selection = random.randint(1, 9) - 1
                good_selection = x.check_validity(selection)
        x.make_turn(selection, player)
        win_state = x.check_for_win(player)
        if win_state is True:
                if player == 1:
                    clear()
                    x.print_board()
                    print("You Win!")
                    if input(" Press Enter to play again, any other key to quit!") == "":
                        x.clear_board()
                        game()
                    break
                else:
                    clear()
                    x.print_board()
                    print("Computer Wins!")
                    if input(" Press Enter to play again, any other key to quit!") == "":
                        x.clear_board()
                        game()
                    break
        full_board = x.check_full_board()
        if full_board is True:
                clear()
                x.print_board()
                print("Nobody Wins!")
                if input(" Press Enter to play again, any other key to quit!") == "":
                    x.clear_board_()
                    game()
                break
        else:
            if player == 1:
                player = 2
            else:
                player = 1


start()
x = TicTacToe()
game()
