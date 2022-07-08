from games import game
from flask import Flask, session, request, redirect, url_for, render_template
app = Flask(__name__)
app.secret_key = b'_5#Gc2L"F4Q8z\n\Mec]/'

tictac = game()
board = tictac.start()
@app.errorhandler(404)
def page_not_found(e):
    return "<center><h4>Page Youre looking for doesnt exist - DevPlusZw <a href='/'>go back</></h4></center>"
@app.route('/', methods=['GET', 'POST'])
def index():
    player = tictac.check_win()
    if request.method == 'POST':
        player = request.form['player']
        pos = request.form['pos']
        return redirect(url_for('index', board=player, player=pos))
    return render_template('index.html', board=board, player=player)
@app.route('/gameover')
def gameover():
    return "game over" 
# game funtion

if __name__ == "__main__":
    app.run()
