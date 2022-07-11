class game:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #3 rows and 3 colums for the game

        self.player1 = "X"
        self.player2 = "0"
        self.turn = player1 
        self.winner = None
        self.count = 0
        self.game_over = False
    def start(self):
        
        y = self.count
        return {"1" : self.board , "2" : y}
        # return "titac" + str(self.count)#just for testing function call
        #start the game logic

    def move_valid(self, pos):
        if pos >= 0 and pos <= 8 and self.board[pos] == " ":
            return 'valid'
        else:
            return 'not valid'
        #check if move valid

    def check_win(self):
        if board[0] == board[1] == board == board[2] == self.player1: #horizontal 1 check
               return win
        if board[0] == board[1] == board == board[2] == self.player2: #horizontal 1 check
               return win
        if board[3] == board[4] == board == board[5] == self.player1: #horizontal 1 check
               return win
        if board[3] == board[4] == board == board[5] == self.player2: #horizontal 1 check
               return win
        if board[6] == board[7] == board == board[8] == self.player1: #horizontal 1 check
               return win
        if board[6] == board[7] == board == board[8] == self.player2: #horizontal 1 check
               return win
        #check if game is over and someone won

    def apply_move(self, pos, turn):
        self.board[pos] = turn
        self.count += 1
        #input move to board
    def switch(self):
        if self.turn == self.player1:
            self.turn == self.player2
        else:
            self.turn == self.player
        return self.turn
