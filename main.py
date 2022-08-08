from re import A
from flask import Flask
app = Flask(__name__)
@app.route('/')
def name():
    return "Pratyusha Chaudhari"


if __name__ == "__main__":
    app.run(debug=True)