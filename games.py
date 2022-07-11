class game:
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
        if self.board[0] == self.board[1] == self.board == self.board[2] == "X": #horizontal 1 check
               self.gameon = False
               return "win"
        if self.board[0] == self.board[1] == self.board == self.board[2] == "0": #horizontal 1 check
               self.gameon = False
               return "win"
        if self.board[3] == self.board[4] == self.board == self.board[5] == "X": #horizontal 1 check
               self.gameon = False
               return "win"
        if self.board[3] == self.board[4] == self.board == self.board[5] == "0": #horizontal 1 check
               self.gameon = False
               return "win"
        if self.board[6] == self.board[7] == self.board == self.board[8] == "X": #horizontal 1 check
               self.gameon = False
               return "win"
        if self.board[6] == self.board[7] == self.board == self.board[8] == "0": #horizontal 1 check
               self.gameon = False
               return "win"

        if self.count == 9:
            self.gameon = False
            return "draw"
        #check if game is over and someone won...add other check validations
    def check_gameon(self):
        return self.gameon
    def apply_move(self, pos):
        self.board[pos] = self.turn
        self.count += 1
        #input move to board
    def switch(self):
        if self.turn == self.player1:
            self.turn == self.player2
        else:
            self.turn == self.player
        return self.turn
