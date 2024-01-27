from bson import ObjectId
from flask import jsonify
from model.comment import Comment

class CmtController:
    @staticmethod
    def create_comment(mongo, request):
        try:
            content = request.json['content']
            user_id = request.json['idUser']
            book_id = request.json['idBook']
            rating = request.json['rating']

            cmt_collection = mongo.db.comments
            account_collection = mongo.db.accounts

            account = account_collection.find_one({'_id': ObjectId(user_id)})

            user_cmt= {}
            user_cmt['_id'] = str(account['_id'])
            user_cmt['username'] = account['username']
            user_cmt['image'] = account['image']

            comment = Comment(content=content, user = user_cmt, book = book_id, 
                            rating=rating)
            result = cmt_collection.insert_one(comment.__dict__)

            inserted_comment = cmt_collection.find_one({'_id': result.inserted_id})

            inserted_comment['_id'] = str(inserted_comment['_id'])

            return jsonify({'data': inserted_comment, 'statusCode': 200, 'message': 'Comment added successfully'})
        except Exception as e:
            return jsonify({'statusCode': 500, 'message': str(e)})

    @staticmethod
    def get_comment_of_book(mongo, request):
        id_book = request.args.get('idBook')
        cmt_collection = mongo.db.comments

        cmts = list(cmt_collection.find({'book': id_book}))

        for cmt in cmts:
            cmt['_id'] = str(cmt['_id'])

        if not cmts:
            return jsonify({'message': 'Book has not comment'})
        else:
            return jsonify({'data': cmts})
        
    @staticmethod
    def like_comment(mongo, request):
        id_cmt = request.json['idCmt']
        id_user = request.json['idUser']
        comment_collection = mongo.db.comments

        cmt = comment_collection.find_one({'_id': ObjectId(id_cmt)})

        number_like = cmt['like'] + 1
        interact = cmt['interact']

        if not interact:
            interact = []
        interact.append(id_user)

        result = comment_collection.update_one({'_id': ObjectId(id_cmt)}, 
                {'$set': {'like': number_like, 'interact': interact}})

        if result.modified_count > 0:
            return jsonify({'message': 'Success'})
        else:
            return jsonify({'message': 'Failed'})
        
    @staticmethod
    def dislike_comment(mongo, request):
        id_cmt = request.json['idCmt']
        id_user = request.json['idUser']

        comment_collection = mongo.db.comments

        cmt = comment_collection.find_one({'_id': ObjectId(id_cmt)})

        number_like = cmt['like'] - 1
        interact = cmt['interact']

        interact.remove(id_user)

        result = comment_collection.update_one({'_id': ObjectId(id_cmt)},
                    {'$set': {'like': number_like, 'interact': interact}})
        
        if result.modified_count > 0:
            return jsonify({'message': 'Success'})
        else:
            return jsonify({'message': 'Failed'})

    @staticmethod
    def is_rating(mongo, request):
        id_book = request.args.get('idBook')
        id_user = request.args.get('idUser')

        comment_collection = mongo.db.comments

        cmts = list(comment_collection.find({'book': id_book}))

        for cmt in cmts:
            user = cmt['user']
            if str(user['_id']) == id_user:
                return jsonify({'message': 'Evaluated'})
            
        return jsonify({'message': 'Not yet rated'})
