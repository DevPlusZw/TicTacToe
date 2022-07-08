class game:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] #3 rows and 3 colums for the game
        self.turn = "X" #for default player 1 turn
        self.player1 = "X"
        self.player2 = "0"
        self.winner = None
        self.count = 0
        self.game_over = False
    def start(self):
        self.count += 1
        return "titac" + str(self.count)#just for testing function call
        #start the game logic

    def move_valid(self):
        return 'valid or not valid'
        #check if move valid

    def check_win(self):
        return self.player1
        #check if game is over and someone won

    def apply_move(self, pos):
        return 'apply move' + str(pos)
        #input move to board
