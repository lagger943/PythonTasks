import os,sys
import subprocess
import shutil
import random

columns = shutil.get_terminal_size().columns
def clear(): 
  
    if os.name == 'nt': 
        _ = os.system('cls')  
    else: 
        _ = os.system('clear') 
        
def Start():
    print("\n")
    print("\t\t\t\t▓▓▓▓▓ ▓ ▓▓▓▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓\n\t\t\t\t  ▓     ▓        ▓    ▓ ▓  ▓         ▓   ▓   ▓ ▓    \n\t\t\t\t  ▓   ▓ ▓    ▓   ▓   ▓   ▓ ▓     ▓   ▓   ▓   ▓ ▓▓▓▓▓\n\t\t\t\t  ▓   ▓ ▓        ▓   ▓▓▓▓▓ ▓         ▓   ▓   ▓ ▓    \n\t\t\t\t  ▓   ▓ ▓▓▓▓     ▓   ▓   ▓ ▓▓▓▓▓     ▓   ▓▓▓▓▓ ▓▓▓▓▓\n")
    print("\n How to play:\n You play this game with numpad of the keyboard. Number placement corresponds to the columns in the game. Example:\n",end='')
    print("   ┌───┬───┬───┐\n   │ 7 │ 8 │ 9 │\n   │───┼───┼───┤\n   │ 4 │ 5 │ 6 │\n   ├───┼───┼───┤\n   │ 1 │ 2 │ 3 │\n   └───┴───┴───┘\n",end='')
    print(" The game could be played PvP, or versus computer\n Type 1 for PvP, 2 to play vs computer and 3 to exit\n",end='')
    choice = input(" Enter your choice:")
    if choice == '1' :
        TwoPlayers()
    elif choice == '2':
        SinglePlayer()
    elif choice == '3':
        pass
    else: 
        clear()
        Start()

def TwoPlayers():
    clear()
    gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 1
    il = 0
    while il == 0:
        print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
        print(f" Player {player} turn!")
        pinput = input(" Enter your choice:")
        selection = int(pinput) - 1
        if selection not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or gameboard[selection] != ' ':
            clear()
            continue
        if player == 2:
            gameboard[selection] = 'X'
        else: 
            gameboard[selection] = 'O'
        clear()
        if gameboard[6] == gameboard[7] == gameboard[8] != ' ' or gameboard[3] == gameboard[4] == gameboard[5] != ' ' or gameboard[0] == gameboard[1] == gameboard[2] != ' ' or gameboard[8] == gameboard[5] == gameboard[2] != ' ' or gameboard[7] == gameboard[4] == gameboard[1] != ' ' or gameboard[6] == gameboard[3] == gameboard[0] != ' ' or gameboard[0] == gameboard[4] == gameboard[8] != ' ' or gameboard[6] == gameboard[4] == gameboard[2] != ' ':
            clear()
            print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
            print(f" Player {player} Wins!")
            choice = input(" Enter 1 to play again or any other key to go back to Start:")
            if choice == '1' :
                TwoPlayers()
            clear()
            Start()
        if ' ' not in gameboard:
            clear()
            print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
            print(" Nobody Wins!")
            choice = input(" Enter 1 to play again or any other key to go back to Start:")
            if choice == '1' :
                TwoPlayers()
            clear()
            Start()
        if player == 1: player = 2
        else: player = 1
        clear()
        
def SinglePlayer():
    clear()
    gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 1
    il = 0
    while il == 0:
        print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
        print(f" It's your turn!")
        if player == 1:
            pinput = input(" Enter your choice:")
            selection = int(pinput) - 1
            if selection not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or gameboard[selection] != ' ':
                clear()
                continue
            gameboard[selection] = 'O'
        else:
            number = random.randint(1,9)
            selection = number - 1
            if gameboard[selection] != ' ':
                clear()
                continue
            else: gameboard[selection] = 'X'
        if gameboard[6] == gameboard[7] == gameboard[8] != ' ' or gameboard[3] == gameboard[4] == gameboard[5] != ' ' or gameboard[0] == gameboard[1] == gameboard[2] != ' ' or gameboard[8] == gameboard[5] == gameboard[2] != ' ' or gameboard[7] == gameboard[4] == gameboard[1] != ' ' or gameboard[6] == gameboard[3] == gameboard[0] != ' ' or gameboard[0] == gameboard[4] == gameboard[8] != ' ' or gameboard[6] == gameboard[4] == gameboard[2] != ' ':
            clear()
            print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
            if player == 1:
                print(" You win!")
            else: print(" Computer Wins!")
            choice = input(" Enter 1 to play again or any other key to go back to Start:")
            if choice == '1' :
                TwoPlayers()
            clear()
            Start()
        if ' ' not in gameboard:
            clear()
            print(f"   ┌───┬───┬───┐\n   │ {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} │\n   │───┼───┼───┤\n   │ {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} │\n   ├───┼───┼───┤\n   │ {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} │\n   └───┴───┴───┘\n",end='')
            print(" Nobody Wins!")
            choice = input(" Enter 1 to play again or any other key to go back to Start:")
            if choice == '1' :
                TwoPlayers()
            clear()
            Start()
        if player == 1: player = 2
        else: player = 1
        clear()
Start()