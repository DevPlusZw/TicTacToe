from games import game
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = b'_5#Gc2L"F4Q8z\n\Mec]/'

mysession = 'mysession'
error = '' #set to pass errors to UI
tictac = game()
pos = 0

@app.before_request
def starter():
    # having fun with request headers
    toV2 = request.headers
    print(tictac.passw)
    allowed = ['gameover', 'gamon']
    if "Sec-Ch-Ua-Platform" in toV2:
        SvG9 = toV2["Sec-Ch-Ua-Platform"]
        btv1 = SvG9.replace('"', '')
        print(btv1)
        if btv1 != "macOS":
            return "invalid btv1"
    print(toV2)
    if request.endpoint not in allowed:
        return "<h1>Not allowed to view this page</h1>"
    print("before")
   
    

@app.errorhandler(404)
def page_not_found(e):
    return "<center><h4>Page Youre looking for doesnt exist - DevPlusZw <a href='/'>go back</a></h4></center>"


@app.route('/', methods=['GET', 'POST'])
def gamon():
    session['game'] = mysession
    print(session['game'])
    error = ''
    data = tictac.start()
    board = data['1']
    num = data['2']
    player = tictac.get_player()
    pos = 0
    if request.method == 'POST':
        player = tictac.get_player()
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
                        session.pop('game', None)
                        tictac.restart()
                        return render_template('index.html', board=board, player=player, num=num, error=error, over='over')
                    elif tictac.check_win() == "draw":
                        error = "Draw! its a Tie"
                        session.pop('game', None)
                        tictac.restart()
                        return render_template('index.html', board=board, player=player, num=num, error=error, over='over')
                        print("draw")
                    else:
                        print("gameon")
                        #for draw
                        data =tictac.start()
                        num = data['2']
                        tictac.switch()
                        player = tictac.get_player()
                else:
                    error = "IVALID POSITION PLAYED, TRY AGAIN"
            return render_template('index.html', board=board, player=player, num=num, error=error)
    return render_template('index.html', board=board, player=player, num=num, error=error)


@app.route('/Score')
def gameover():
    tictac.gameon = False
    print("game over") 
    return "<h1><u>Score Board | TicTacToe by DevPlusZw</u> &copy 2022 - DevPlusZw <a href='/'>go back</a></h1>" 
# game funtion

if __name__ == "__main__":
    app.run(debug=True)
