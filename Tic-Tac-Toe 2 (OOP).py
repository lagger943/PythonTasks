import os,sys
import random

class TicTacToe:
    def __init__(self):
        self.GameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.PlayerPTS = 0
        self.CompPTS = 0
    
    def PrintBoard(self):
        print(f" Your wins: {self.PlayerPTS} | Computer Wins: {self.CompPTS}")
        print(f"   ┌───┬───┬───┐\n   │ {self.GameBoard[6]} │ {self.GameBoard[7]} │ {self.GameBoard[8]} │\n   │───┼───┼───┤\n   │ {self.GameBoard[3]} │ {self.GameBoard[4]} │ {self.GameBoard[5]} │\n   ├───┼───┼───┤\n   │ {self.GameBoard[0]} │ {self.GameBoard[1]} │ {self.GameBoard[2]} │\n   └───┴───┴───┘\n",end='')
        
    def AddPlayerPTS(self):
        self.PlayerPTS = self.PlayerPTS + 1
    
    def AddCompPTS(self):
        self.CompPTS = self.CompPTS + 1
    
    def CheckValidity(self,selection):
        if selection not in range(0,9) or self.GameBoard[selection] != ' ':
            return False
        else: 
            return True
            
    def MakeATurn(self,selection,player):
        if player == 1:
            self.GameBoard[selection] = 'X'
        else:
            self.GameBoard[selection] = '0'
    
    def CheckForWin(self,player):
        if self.GameBoard[6] == self.GameBoard[7] == self.GameBoard[8] != ' ' or self.GameBoard[3] == self.GameBoard[4] == self.GameBoard[5] != ' ' or self.GameBoard[0] == self.GameBoard[1] == self.GameBoard[2] != ' ' or self.GameBoard[8] == self.GameBoard[5] == self.GameBoard[2] != ' ' or self.GameBoard[7] == self.GameBoard[4] == self.GameBoard[1] != ' ' or self.GameBoard[6] == self.GameBoard[3] == self.GameBoard[0] != ' ' or self.GameBoard[0] == self.GameBoard[4] == self.GameBoard[8] != ' ' or self.GameBoard[6] == self.GameBoard[4] == self.GameBoard[2] != ' ':
            if player == 1:
                self.AddPlayerPTS()
            else:
                self.AddCompPTS()
            return True
        else:
            return False
            
    def CheckForFullBoard(self):
            if ' ' not in self.GameBoard:
                return True
            else:
                return False
                
    def ClearBoard(self):
        for i in range(len(self.GameBoard)):
            self.GameBoard[i] = ' '
            
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
    os.system("pause")

def Game():
    clear()
    il = 0
    if random.randint(1,20) > 10:
        player = 1
    else: 
        player = 2
    while il == 0:
        gs = False
        winstate = False
        fullboard = False
        while gs == False:
            if player == 1:
                clear()
                x.PrintBoard()
                pinput = input(" Enter your choice:")
                if pinput == "":
                    clear()
                    continue
                selection = int(pinput) - 1
                gs = x.CheckValidity(selection)
                
            else:
                number = random.randint(1,9)
                selection = number - 1
                gs = x.CheckValidity(selection)
        x.MakeATurn(selection,player)
        winstate = x.CheckForWin(player)
        if winstate == True :
                if player == 1:
                    clear()
                    x.PrintBoard()
                    print("You Win!")
                    if input(" Press Enter to play again, any other key to quit!") == "":
                        x.ClearBoard()
                        Game()
                    break
                else:
                    clear()
                    x.PrintBoard()
                    print("Computer Wins!")
                    
                    if input(" Press Enter to play again, any other key to quit!") == "":
                        x.ClearBoard()
                        Game()
                    break
        fullboard = x.CheckForFullBoard()
        if fullboard == True:
                clear()
                x.PrintBoard()
                print("Nobody Wins!")
                if input(" Press Enter to play again, any other key to quit!") == "":
                    x.ClearBoard()
                    Game()
                break
        else:
            if player == 1: 
                player = 2
            else: 
                player = 1
     
Start()
x = TicTacToe()
Game()
    
