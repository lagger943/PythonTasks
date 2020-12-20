import os
import random


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear_board')


def dice_print(number):
    if number == 1:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █           █\n   █           █\n   █     ■     █"
              "\n   █           █\n   █           █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')

    elif number == 2:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■         █\n   █           █\n   █           █"
              "\n   █           █\n   █         ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')

    elif number == 3:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■         █\n   █           █\n   █     ■     █"
              "\n   █           █\n   █         ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')

    elif number == 4:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■       ■ █\n   █           █\n   █           █"
              "\n   █           █\n   █ ■       ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')

    elif number == 5:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■       ■ █\n   █           █\n   █     ■     █"
              "\n   █           █\n   █ ■       ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')

    else:
        print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■       ■ █\n   █           █\n   █ ■       ■ █"
              "\n   █           █\n   █ ■       ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')


def single_player():
    while 1:
        clear()
        print("Your rolled:")
        number = random.randint(100000, 600000) // 100000
        dice_print(number)
        if input("To row again press enter") != "":
            break


def multi_player():
    player_pts = 0
    computer_pts = 0
    while 1:
        clear()
        print("\n You rolled:")
        player = random.randint(100000, 600000) // 100000
        dice_print(player)
        print("\n Computer rolled:")
        computer = random.randint(1000, 6000) // 1000
        dice_print(computer)
        if player > computer:
            player_pts += 1
        elif player < computer:
            computer_pts += 1
        print(f" Your wins: {player_pts} | Computer Wins: {computer_pts}")
        if input(" To row again press enter") != "":
            break


def start():
    print("   █▀▀▀▀▀▀▀▀▀▀▀█\n   █ ■       ■ █\n   █           █\n   █ ■       ■ █"
          "\n   █           █\n   █ ■       ■ █\n   █▄▄▄▄▄▄▄▄▄▄▄█\n", end='')
    print("\n Welcome to the dice game\n Type 1 to roll a dice, or 2 to play vs computer", end='')
    selection = input("\n Please make a selection:")
    number = int(selection)
    if selection == '1':
        single_player()
    elif selection == '2':
        multi_player()
    else:
        clear()
        start()


start()
