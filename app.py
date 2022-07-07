from flask import Flask 
app = Flask(__name__)

@app.route('/') #corrected double route error
def method_name():
    return "<h1>TicTacToe Game By devplus</h1>"
    # to add template rendering for initial game
    # 
@app.errorhandler(404)
def page_not_found(e):
    return "<center><h1>Hakuna Page Rakadaro</h1></center>"

if __name__ == "__main__":
    app.run()
