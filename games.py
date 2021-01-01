class game:
    passw = 'i will never use this pass....'
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #3 rows and 3 colums for the game

        self.player1 = "X"
        self.player2 = "0"
        self.turn = self.player1
        self.winner = None
        self.count = 0
        self.gameon = True


    def start(self):
        y = self.count
        return {"1" : self.board , "2" : y}
        # return "titac" + str(self.count)#just for testing function call
        #start the game logic


    def move_valid(self, pos):
        if pos >= 0 and pos <= 8 and self.board[pos] == " ":
            return True
        else:
            return False
        #check if move valid

    def get_player(self):
        return self.turn


    def check_win(self):
        if (self.board[0] == self.board[1] == self.board[2]) and (self.board[0] == "X" or self.board[0] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"

        if (self.board[3] == self.board[4] == self.board[5]) and (self.board[3] == "X" or self.board[3] == "0") : #horizontal 1 check
               self.gameon = False
               return "win"

        if (self.board[6] == self.board[7] == self.board[8]) and (self.board[6] == "X" or self.board[6] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"

        if (self.board[0] == self.board[4] == self.board[8]) and (self.board[4] == "X" or self.board[4] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"

        if (self.board[6] == self.board[4] == self.board[2]) and (self.board[6] == "X" or self.board[6] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"
        
        if (self.board[0] == self.board[3] == self.board[6])  and (self.board[3] == "X" or self.board[3] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"
            
        if (self.board[1] == self.board[4] == self.board[7])  and (self.board[7] == "X" or self.board[7] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"
        
        if (self.board[2] == self.board[5] == self.board[8])  and (self.board[8] == "X" or self.board[8] == "0"): #horizontal 1 check
               self.gameon = False
               return "win"

        if self.count == 9: #check for draw
            self.gameon = False
            return "draw"
        #check win function is over


    def check_gameon(self):
        return self.gameon

    def apply_move(self, pos):
        self.board[pos] = self.turn
        self.count += 1
        #input move to board and increase counter for drwa check

    def switch(self):
        if self.turn == self.player1:
            self.turn = self.player2
            print(self.turn)
        else:
            self.turn = self.player1
            print(self.turn)
        return self.turn
    def restart(self):
        print("restart")
        self.__init__()
   
