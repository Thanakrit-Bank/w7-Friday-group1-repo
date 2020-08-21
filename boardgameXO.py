class Board:
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.getMark = {'1': 'X', '2': 'O'}
        self.player = 2
        self.index = ""

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")

        while (self.round < 10):
            if self.player == "" or self.player == 2:
                mark = self.getMark[str(self.player)]
                pos = int(input("Player 1 turn \nEnter your position 'X': "))
            
            else :
                self.player == 1
                mark = self.getMark[str(self.player)]
                pos = int(input("Player 2 turn \nEnter your position 'O': "))

            class3.placeMarker(mark, pos)
            class2.drawBoard()

            if self.winCheck(self.player) == False:
                self.round += 1
                
                if self.player == 1:
                    self.player = 2
                else: 
                    self.player = 1 
            
            else:
                print("!!!Game Over!!!")
                break

        else:
            print("No player win :( \n!!!Game Over!!!")
            
    def setBoard(self, marker, position): ## ได้ None 
        if position <= 3 and self.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = marker
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = marker
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = marker

        else:
            return False

    def retrieveValue(self, position): ## get value form listBoard
        if position <= 3 and self.listBoard[0][position-1] == " ":
            return self.listBoard[0][position-1]
                
        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            return self.listBoard[1][position-4]
        
        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            return self.listBoard[2][position-7]
        
    def winCheck(self, player): ## check winner
        for i in range(len(self.listBoard)):

            if self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " " or \
               self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " " or \
               self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " " or \
               self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " ":
                
                print("------ Player {} is winner!------".format(self.player))
                return True
        
        if self.player != "":  ## No player has win
            return False

    def clearBoard(self): 
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]

class Printer:       
    def drawBoard(self): ## display board
        for i in range(1,10,3):
            print(class1.retrieveValue(i), " | ", class1.retrieveValue(i+1), " | ", class1.retrieveValue(i+2))
    
class TextInput: 
    def placeMarker(self, marker, position): ## place the marker in list of board
        class1.setBoard(marker, position)
        
        """
        if class1.setBoard(position, player) == False:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.placeMarker(player, pos)
        else:
            pass
        """
    
    """
    def placeMarker(self, player, position): ## place the marker in list of board
        if position <= 3 and class1.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = player
                
        elif 3 < position <= 6 and class1.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = player
        
        elif 6 < position <= 9 and class1.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = player

        else:
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.placeMarker(player, pos)
    """

class1 = Board()
class2 = Printer()
class3 = TextInput()

play = Board()
play.startGame()