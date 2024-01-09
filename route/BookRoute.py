from flask import request
from controller.BookController import BookController

def config_routes(app, mongo):
    @app.route('/get_books', methods = ['GET'])
    def get_books():
        response = BookController.get_all_books(
            mongo = mongo, 
        )
        return response

    @app.route('/get_book_propose', methods = ['GET'])
    def get_book_propose():
        response = BookController.get_book_propose(
            mongo = mongo, 
        )
        return response

    @app.route('/get_books_by_key', methods = ['GET'])
    def get_book_by_key():
        response = BookController.get_book_by_key(
            mongo = mongo, 
            request = request
        )
        return response

    @app.route('/get_book_by_id', methods = ['GET'])
    def get_book_by_id():
        response = BookController.get_book_by_id(
            mongo = mongo, 
            request = request
        )
        return response
    
    @app.route('/get_book_by_type', methods = ['GET'])
    def get_book_by_type():
        response = BookController.get_book_by_type(
            mongo = mongo,
            request = request
        )
        return response

    @app.route('/get_book_propse_by_id', methods = ['GET'])
    def get_book_propse_by_id():
        response = BookController.get_book_propse_by_id(
            mongo = mongo,
            request = request
        )

        return response
    
    @app.route('/get_book_propse_by_author', methods = ['GET'])
    def get_book_propse_by_author():
        response = BookController.get_book_propse_by_author(
            mongo = mongo,
            request = request
        )

        return response