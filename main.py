import numpy as np
import random

class Game:
    def __init__(self):
        self.board_names = '''
        a     b     c
           |     |     
    1  1a  | 1b  |  1c 
      _____|_____|_____
           |     |     
    2  2a  | 2b  |  2c 
      _____|_____|_____
           |     |     
    3  3a  | 3b  |  3c 
           |     |     
    '''
        self.signs = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.a = 0
        self.b = 1
        self.c = 2

        print("Welcome in Tic Tac Toe!\nHere's our board")
        print(self.board_names)
    
    def take_input(self):
        user_input = input("Enter the field name(example: 2b)>> ")
        if(self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] != 'O'):
            self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] = "X"
        else:
            print("You can't do that! Enter the field name again")
            print(np.matrix(game.signs))
            self.take_input()

    def draw_position(self):
        self.o_position = []
        for i in range(0,2):
            self.o_position.append(random.randint(0,2))
        return self.o_position
    
    def place_cricle(self):
        postion = self.draw_position()
        if (self.signs[postion[0]][postion[1]] != "X"):
            self.signs[postion[0]][postion[1]] = 'O'
        else:
            self.place_cricle()
    
    def check_win(self):
        if(self.signs[0][0] != '-' and [self.signs[0][0]] * len(self.signs[0]) == self.signs[0]):
            if(self.signs[0][0] == 'X'): 
                print("YOU WON!!!")
            else:
                print("You lost")
            return True
        elif(self.signs[1][0] != '-' and [self.signs[1][0]] * len(self.signs[1]) == self.signs[1]):
            if(self.signs[1][0] == 'X'):
                print("YOU WON!!!")
            else:
                print("You lost")

END = False
print("-----------------------------------------------------------------")
game = Game()
while END == False:
    print("-----------------------------------------------------------------")
    game.take_input()
    game.place_cricle()
    if(game.check_win()):
        END = True
    print(np.matrix(game.signs))
