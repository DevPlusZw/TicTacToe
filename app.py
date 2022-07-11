from games import game
from flask import Flask, session, request, redirect, url_for, render_template
app = Flask(__name__)
app.secret_key = b'_5#Gc2L"F4Q8z\n\Mec]/'

mysession = 'mysession'

error = '' #set to pass errors to UI
tictac = game()
pos = 0
@app.errorhandler(404)
def page_not_found(e):
    return "<center><h4>Page Youre looking for doesnt exist - DevPlusZw <a href='/'>go back</></h4></center>"
@app.route('/', methods=['GET', 'POST'])
def gamon():
    session['game'] = mysession
    error = ''
    player = tictac.get_player()
    data = tictac.start()
    board = data['1']
    num = data['2']
    pos = 0
    if request.method == 'POST':
        player = request.form['player']
        if tictac.check_gameon():
            if request.form['pos'] == "":
                print('error on pos')
            else:  
                player = tictac.get_player()
                pos = int(request.form['pos'])
                if tictac.move_valid(pos):
                    tictac.apply_move(pos)
                    if tictac.check_win() == "win":
                        #for win
                        error = "Gameover! " + str(player) + " won."
                        print("win")
                    elif tictac.check_win() == "draw":
                        error = "Draw! its a Tie"
                        print("draw")
                        
                    else:
                        print("gameon")
                        #for draw
                    data =tictac.start()
                    num = data['2']
                    tictac.switch()
                else:
                    error = "IVALID POSITION PLAYED, TRY AGAIN"
            return render_template('index.html', board=board, player=player, num=num, error=error)
    return render_template('index.html', board=board, player=player, num=num, error=error)
@app.route('/gameover')
def gameover():
    return "game over" 
# game funtion

if __name__ == "__main__":
    app.run(debug=True)
