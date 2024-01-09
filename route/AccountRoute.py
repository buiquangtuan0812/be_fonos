from flask import request
from controller.AccountController import AccountController

def config_routes(app, mongo):
    @app.route('/register', methods=['POST'])
    def register():
        response = AccountController.signup(
            mongo = mongo,
            request = request
        )
        return response

    @app.route('/login', methods=['POST'])
    def login():
        response = AccountController.login(
            mongo = mongo,
            request = request
        )
        return response

    @app.route('/update_profile', methods=['PUT'])
    def update_profile():
        response = AccountController.update_profile(
            mongo = mongo,
            request = request
        )
        return response

    @app.route('/like_book', methods = ['POST'])
    def like_book():
        response = AccountController.like_book(
            mongo = mongo,
            request = request
        )

        return response
    
    @app.route('/dislike_book', methods = ['POST'])
    def dislike_book():
        response = AccountController.dislike_book(
            mongo = mongo,
            request = request
        )

        return response
