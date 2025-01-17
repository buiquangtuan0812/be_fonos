from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from route import account_route, book_route, author_route, cmt_route

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/fonos_db'

mongo = PyMongo(app)
app.config['PORT'] = 8080
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET, POST, PUT, PATCH, DELETE')
    return response

account_route.config_routes(app, mongo)
book_route.config_routes(app, mongo)
author_route.config_routes(app, mongo)
cmt_route.config_routes(app, mongo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)