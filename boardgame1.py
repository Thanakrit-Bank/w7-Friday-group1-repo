
class TicTocToe:
    def __init__ (self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.all_player = {'X':'Player 1', 'O':'Player 2', 'player1':'X', 'player2':'O'}
        self.player = ""

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")
        
        while (self.round < 10):
            
            if self.player == "" or self.player == self.all_player['player2'] :
                self.player = self.all_player['player1']
                pos = int(input("Player 1 turn \nEnter your position 'X': "))

            else:
                self.player = self.all_player['player2']
                pos = int(input("Player 2 turn \nEnter your position 'O': "))
            
            self.place_marker(self.player, pos)
            self.display_board()
            
            if self.win_check(self.player) == True:
                    self.round += 1
            
            else:
                print("End game")
                break
        
        else:
            print("No player win :( \nEnd game")

    def place_marker(self, user, position):
        if position <= 3 and self.board[0][position-1] == " ":
            self.board[0][position-1] = user
                
        elif 3 < position <= 6 and self.board[1][position-4] == " ":
            self.board[1][position-4] = user
        
        elif 6 < position <= 9 and self.board[2][position-7] == " ":
            self.board[2][position-7] = user

        else:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.place_marker(user, pos)

    def display_board(self):
        for i in range(len(self.board)):
            print(self.board[i][0], " | ", self.board[i][1], " | ", self.board[i][2])

    def win_check(self, user): 
        for i in range(len(self.board)):
            if (self.board[0][0] == self.board[1][1] == self.board[2][2] != " ") or \
            (self.board[0][2] == self.board[1][1] == self.board[2][0] != " ") or \
            (self.board[i][0] == self.board[i][1] == self.board[i][2] != " ") or \
            (self.board[0][i] == self.board[1][i] == self.board[2][i] != " "):
                
                print("------ {} is winner!------".format(self.all_player[user]))
                return False
        
        if self.player != "":  ## No player has win
            return True

    def ask_toplay(self, answer): 
        if answer == 'Y' or answer == 'y':
            return True
        else:
            return False

test = TicTocToe()
test.startGame()