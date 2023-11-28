from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from controller.AccountController import AccountController

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/fonos_db'

mongo = PyMongo(app)

@app.route('/', methods = ['GET'])
def get_data():
    data = mongo.db.books.find()
    return render_template('index.html', books=data)

@app.route('/signup', methods = ['POST'])
def signup():
    response = AccountController.signup(
        mongo = mongo,
        request = request
    )
    return response

@app.route('/login', methods = ['POST'])
def login():
    response = AccountController.login(
        mongo = mongo,
        request = request
    )
    return response


if __name__ == '__main__':
    app.run(debug = True)