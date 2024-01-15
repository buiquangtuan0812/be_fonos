from flask import request
from controller.AuthorController import AuthorController

def config_routes(app, mongo):
    @app.route('/get_author_by_name', methods = ['GET'])
    def get_author_by_name():
        response = AuthorController.get_author_by_name(
            monogo = mongo,
            request = request
        )

        return response