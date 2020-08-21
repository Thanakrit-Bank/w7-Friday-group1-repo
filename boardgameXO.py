class Board:
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]] ## create empty board
        self.getMark = { 1 : "X", 2 : "O" }  ## marker of each player
        self.player = "" 
        self.index = "" 

        ## link object together
        self.printer = Printer(self)
        self.textInputor = TextInput(self)

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")

        try:
            while (self.round < 10):
                if self.player == "" or self.player == 2:  
                    ## Player 1 Turn
                    self.player = 1
                    pos = int(input("\nPlayer 1 turn \nEnter your position 'X': "))
                
                else :
                    ## Player 2 Turn
                    self.player = 2
                    pos = int(input("\nPlayer 2 turn \nEnter your position 'O': "))

                self.textInputor.placeMarker(self.player, pos)  ## place marker in position that user entered
                self.printer.drawBoard()  ## display board

                if not(self.winCheck(self.player)):
                    ## no one win 
                    self.round += 1
                
                else:
                    ## when have the winner 
                    print("\n!!! End Game !!!")
                    break

            else:
                print("\nNo player win :( \n!!! Game Over !!!")
        
        except ValueError:
            ## case when entered wrong value, wrong type
            print("\nYou entered wrong value....Game will start again")
            self.clearBoard()
            self.player = ""
            self.startGame()

            
    def setBoard(self, player, position):
        # place marker X,O at position that user entered

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
        
    def winCheck(self, player): 
        # check winner
        # return True when has winner

        for i in range(len(self.listBoard)):
            if (self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " ") or \
            (self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " ") or \
            (self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " ") or \
            (self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " "):
                
                print("\n------ Player {} is winner!------".format(player))
                return True
                    
        ## No player has win
        return False     

    def clearBoard(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]

class Printer:       
    def __init__(self, board_obj):
        self.board = board_obj
        
    def drawBoard(self): ## display board
        print("\n")
        for i in range(1,10,3):
            print(self.board.retrieveValue(i), " | ", self.board.retrieveValue(i+1), " | ", self.board.retrieveValue(i+2))
    
class TextInput:
    def __init__(self,board_obj):
        self.board = board_obj
        
    def placeMarker(self, player, position): ## place the marker in list of board
        if self.board.setBoard(player, position) == False:
            # when enter duplicate position
            print("This position has marker! Please enter other position")
            pos = int(input("Enter your new position : "))
            self.placeMarker(player, pos)

# Start Game ! 
play = Board()
play.startGame()