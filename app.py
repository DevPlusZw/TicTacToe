from games import game
from flask import Flask, session, request, redirect, url_for, render_template
app = Flask(__name__)
app.secret_key = b'_5#Gc2L"F4Q8z\n\Mec]/'

error = '' #set to pass errors to UI
tictac = game()
pos = 0
@app.errorhandler(404)
def page_not_found(e):
    return "<center><h4>Page Youre looking for doesnt exist - DevPlusZw <a href='/'>go back</></h4></center>"
@app.route('/', methods=['GET', 'POST'])
def index():
    error = ''
    player = tictac.check_win()
    data = tictac.start()
    board = data['1']
    num = data['2']
    if request.method == 'POST':
        player = request.form['player']
        if request.form['pos'] == "":
            pos = 0
            print('error on pos')
        else:  
            pos = int(request.form['pos'])
            if pos <= 8 and pos >= 0:
                board[pos] = "X"
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
