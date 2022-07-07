from flask import Flask 
app = Flask(__name__)

@app.route('/') #corrected double route error
def method_name():
    return "TicTacToe Game By devplus"
    # to add template rendering for initial game
    # 

if __name__ == "__main__":
    app.run()
