from flask import request
from controller.cmt_controller import CmtController

def config_routes(app, mongo):
    @app.route('/cmt/comment_book', methods = ['POST'])
    def comment_book():
        response = CmtController.create_comment(
            mongo = mongo,
            request = request
        )

        return response
    
    @app.route('/cmt/get_comment_of_book', methods = ['GET'])
    def get_comment_of_book():
        response = CmtController.get_comment_of_book(
            mongo = mongo,  
            request = request
        )

        return response
    
    @app.route('/cmt/like_comment', methods = ['POST'])
    def like_comment():
        response = CmtController.like_comment(
            mongo = mongo,
            request = request
        )

        return response
    
    @app.route('/cmt/dislike_comment', methods = ['POST'])
    def dislike_comment():
        response = CmtController.dislike_comment(
            mongo = mongo,
            request = request
        )

        return response
    
    @app.route('/cmt/is_rating', methods = ['GET'])
    def is_rating():
        response = CmtController.is_rating(
            mongo = mongo,
            request = request
        )

        return response