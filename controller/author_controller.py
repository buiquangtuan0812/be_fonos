from flask import jsonify
from bson import ObjectId

class AuthorController:
    @staticmethod
    def get_author_by_id(mongo, request):
        id_author = request.args.get('id')
        author_collection = mongo.db.authors

        author = author_collection.find_one({'_id': ObjectId(id_author)})

        if author is None:
            return jsonify({'data': 'Author not found', 'statusCode': 400})
        else:
            author['_id'] = str(author['_id'])
            return jsonify({'data': author, 'statusCode': 200})
        
    def get_author_by_name(monogo, request):
        name_author = request.args.get('name')
        author_collection = monogo.db.authors

        author = author_collection.find_one({'name': name_author})

        if author is None:
            return jsonify({'data': 'Author not found', 'statusCode': 400})
        else:
            author['_id'] = str(author['_id'])
            return jsonify({'data': author, 'statusCode': 200})