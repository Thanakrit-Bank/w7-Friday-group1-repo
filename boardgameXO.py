class Board:
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.getMark = {1: 'X', 2:'O'}
        self.player = 2
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

            class3.placeMarker(self.player, pos)
            class2.drawBoard()

            if self.winCheck() == False:
                self.round += 1

            else:
                print("!!!Game Over!!!")
                break

        else:
            print("No player win :( \n!!!Game Over!!!")
            
    def setBoard(self, position, player):
            if position <= 3 and self.listBoard[0][position-1] == " ":
                self.listBoard[0][position-1] = self.getMark[self.player]
                    
            elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
                self.listBoard[1][position-4] = self.getMark[self.player]
            
            elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
                self.listBoard[2][position-7] = self.getMark[self.player]

            else:
                return False

    def retrieveValue(self, index): ## get value form listBoard
        if position <= 3 and self.listBoard[0][position-1] == " ":
            return self.listBoard[0][position-1]
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            return self.listBoard[1][position-4]
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            return self.listBoard[2][position-7]
        
    def winCheck(self): ## check winner
        for i in range(len(self.listBoard)):
            if self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " " or \
               self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " " or \
               self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " " or \
               self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " ":
                
                print("------ {} is winner!------".format(self.all_player[player]))
                return True
        
        if self.player != "":  ## No player has win
            return False

    def clearBoard(self): 
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]

class Printer: 
    listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
        
    def drawBoard(self): ## display board
        for i in range(len(self.listBoard)):
            ##print(i)
            print(self.listBoard[i][0], " | ", self.listBoard[i][1], " | ", self.listBoard[i][2])
    
class TextInput: 
    listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    # def placeMarker(self, player, position): ## place the marker in list of board
        # while True:
            # class1.setBoard(position, player)
    
    def placeMarker(self, player, position): ## place the marker in list of board
        if position <= 3 and self.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = player
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = player
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = player

        else:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.placeMarker(player, pos)

class1 = Board()
class2 = Printer()
class3 = TextInput()

class1.startGame()
