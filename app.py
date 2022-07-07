from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"


def start_game():
#     to add load board 
# to add get players names
