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
           |     |     '''
        
        self.signs = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
         
        self.letters = ['a', 'b', 'c']

        print("Welcome in Tic Tac Toe!\nHere's our board:")
        print(self.board_names)
    
    def game_mode(self):
        print("Choose game mode:\n 1) player vs player\n 2) player vs bot")
        game_type = input(">>")
        if (game_type == "1" or game_type == "2"):
            return int(game_type)

    def take_input_x(self):
        user_input = input("Enter the field name(example: 2b)>> ")
        if(self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] != 'O'):
            self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] = 'X'
            self.board_names = self.board_names.replace(user_input, ' X')
        else:
            print("You can't do that! Enter the field name again")
            print(self.board_names)
            self.take_input_x()

    def take_input_o(self):
        user_input = input("Enter the field name(example: 2b)>> ")
        if(self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] != 'X'):
            self.signs[int(user_input[0]) - 1][ord(user_input[1]) - 97] = 'O'
            self.board_names = self.board_names.replace(user_input, ' O')
        else:
            print("You can't do that! Enter the filed name again")
            print(self.board_names)
            self.take_input_o()

    def draw_position(self):
        self.o_position = []
        for i in range(0,2):
            self.o_position.append(random.randint(0,2))
        return self.o_position
    
    def place_cricle(self):
        postion = self.draw_position()
        if (self.signs[postion[0]][postion[1]] != 'X'):
            self.signs[postion[0]][postion[1]] = 'O'
            self.board_names = self.board_names.replace(str(postion[0]+1) + self.letters[postion[1]], ' O')
        else:
            self.place_cricle()
    
    #* Main mechanic 

    def check_draw(self):
        check = []
        for i in range(3):
            check.append('-' in self.signs[i])
        return (check[0] == False == check[1] == check[2])

    def check_win(self, player1 = "You", player2 = "Bot"):
        if(self.signs[0][0] != '-' and self.signs[0][0] == self.signs[1][1] == self.signs[2][2]):
            if(self.signs[0][0] == 'X'):
                print(f"{player1} won!!!")
            else:
                print(f"{player2} won!!!")
            return True
        elif(self.signs[0][2] != '-' and self.signs[0][2] == self.signs[1][1] == self.signs[2][0]):
            if(self.signs[0][2] == 'X'):
                print(f"{player1} won!!!")
            else:
                print(f"{player2} won!!!")
            return True
        for i in range(3):
            if(self.signs[i][0] != '-' and [self.signs[i][0]] * len(self.signs[i]) == self.signs[i]):
                if(self.signs[i][0] == 'X'): 
                    print(f"{player1} won!!!")
                else:
                    print(f"{player2} won!!!")
                return True
            if(self.signs[0][i] != '-' and self.signs[0][i] == self.signs[1][i] == self.signs[2][i]):
                if(self.signs[0][i] == 'X'):
                    print(f"{player1} won!!!")
                else:
                    print(f"{player2} won!!!")
                return True
        
        if(self.check_draw()):
            print("It's a draw!")
            return True

END = False
print("-----------------------------------------------------------------")
game = Game()
if(game.game_mode() == 1):
    print("You choose first option, player vs player")
    print("-----------------------------------------------------------------")
    player1_name = input("Enter name of first player: ")
    player2_name = input("Enter name of second player: ")
    rep = 0
    while END == False:
        rep += 1
        print("-----------------------------------------------------------------")
        print(f"{player1_name} turn")
        game.take_input_x()
        if(rep >= 3 and game.check_win(player1 = player1_name, player2 = player2_name)):
            END = True
            print(game.board_names)
            break
        print(game.board_names)
        print("-----------------------------------------------------------------")
        print(f"{player2_name} turn")
        game.take_input_o()
        if(rep >= 3 and game.check_win(player1 = player1_name, player2 = player2_name)):
            END = True
            print(game.board_names)
            break
        print(game.board_names)

else:
    print("You choose second option, player vs bot")
    rep = 0
    while END == False:
        print("-----------------------------------------------------------------")
        game.take_input_x()
        game.place_cricle()
        rep += 1
        if(rep >= 3 and game.check_win()):
            END = True
        print(game.board_names)
