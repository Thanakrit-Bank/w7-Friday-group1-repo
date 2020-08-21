class Board:
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.getMark = { 1 : "X", 2 : "O" }
        self.player = ""
        self.index = ""

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")

        while (self.round < 10):
            if self.player == "" or self.player == 2:
                self.player = 1
                pos = int(input("Player 1 turn \nEnter your position 'X': "))
            
            else :
                self.player = 2
                pos = int(input("Player 2 turn \nEnter your position 'O': "))

            class3.placeMarker(self.player, pos)
            class2.drawBoard()

            if not(self.winCheck(self.player)):
                self.round += 1
            
            else:
                print("!!! End Game !!!")
                break
            print(self.listBoard)
        else:
            print("No player win :( \n!!! Game Over !!!")
            
    def setBoard(self, player, position): ## set marker in board
        if position <= 3 and self.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = self.getMark[player]
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = self.getMark[player]
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = self.getMark[player]

        else:
            return False

    def retrieveValue(self, position): ## get value form listBoard
        if position <= 3 :
            return self.listBoard[0][position-1]
                
        elif 3 < position <= 6 :
            return self.listBoard[1][position-4]
        
        elif 6 < position <= 9 :
            return self.listBoard[2][position-7]
        
    def winCheck(self, player): ## check winner
        for i in range(len(self.listBoard)):
            if (self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " ") or \
            (self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " ") or \
            (self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " ") or \
            (self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " "):
                
                print("\n------ Player {} is winner!------".format(player))
                return True
                    
        ## No player has win
        return False
            

class Printer:       
    def drawBoard(self): ## display board
        for i in range(1,10,3):
            print(class1.retrieveValue(i), " | ", class1.retrieveValue(i+1), " | ", class1.retrieveValue(i+2))
    
class TextInput:
    def placeMarker(self, player, position): ## place the marker in list of board
        if class1.setBoard(player, position) == False:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.placeMarker(player, pos)


# Create object of each class for called in method of other class       
class1 = Board()
class2 = Printer()
class3 = TextInput()

# Start Game ! 
class1.startGame()