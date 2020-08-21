class Board:
    def __init__(self):
        self.getMark = {1: 'X', 2:'O'}

        self.player = 1
        self.index = ""

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")

        while (self.round < 10):
            if self.player == "" or self.player == 2:
                self.mark = self.getMark[self.player]
                pos = int(input("Player 1 turn \nEnter your position 'X': "))
            
            else :
                self.player == 1
                self.mark = self.getMark[self.player]
                pos = int(input("Player 2 turn \nEnter your position 'O': "))

    def setBoard(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def retrieveValue(self, index): ## method อันนี้ทำไรนะะ //getter ปะ? ของ Value
        if position <= 3 and self.listBoard[0][position-1] == " ":
            return self.listBoard[0][position-1]
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            return self.listBoard[1][position-4]
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            return self.listBoard[2][position-7]
    
    def winCheck(self, round):
        for i in range(len(self.listBoard)):
            if self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " " or \
               self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " " or \
               self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " " or \
               self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " ":
                
                print("------ {} is winner!------".format(self.all_player[player]))
                return False
        
        if self.player != "":  ## No player has win
            return True

    def clearBoard(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]

class Printer:
    def drawBoard(self):
        for i in range(len(self.listBoard)):
            print(self.listBoard[i][0], " | ", self.listBoard[i][1], " | ", self.listBoard[i][2])
    
class TextInput:
    def placeMarker(self, player):
        if position <= 3 and self.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = player
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = player
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = player

        else:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.place_marker(player, pos)