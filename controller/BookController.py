from flask import jsonify
from bson import ObjectId
import random

class BookController:
    @staticmethod
    def get_all_books(mongo):
        book_collection = mongo.db.books
        books = list(book_collection.find())
        for book in books:
            book['_id'] = str(book['_id'])

        if books is None:
            return jsonify({'message': 'Book not found', 'statusCode': 400})
        else:
            return jsonify({'data': books, 'statusCode': 200})
        
    @staticmethod
    def get_book_by_key(mongo, request):
        book_collection = mongo.db.books
        key = request.args.get('key')
        query = {'name': {'$regex': key, '$options': 'i'}}
        books = list(book_collection.find(query))
        for book in books:
            book['_id'] = str(book['_id'])

        if books is None:
            return jsonify({'message': 'Book not found', 'statusCode': 404})
        else:
            return jsonify({'data': books, 'statusCode': 200})
            
    
    @staticmethod
    def get_book_by_id(mongo, request):
        book_collection = mongo.db.books
        id_book = request.args.get('id')
        object_id = ObjectId(id_book)
        book = book_collection.find_one({'_id': object_id})

        if book is not None:
            book['_id'] = str(book['_id'])
            return jsonify({'data': book, 'statusCode': 200})
        else:
            return jsonify({'message': 'Book not found', 'statusCode': 404})
    
    @staticmethod
    def get_book_propose(mongo):
        book_collection = mongo.db.books
        books = list(book_collection.find())
        book_random = random.sample(books, 8)
        for value in book_random:
            value['_id'] = str(value['_id'])
        return jsonify({'data': book_random, 'statusCode': 200})
    
    @staticmethod
    def get_book_by_type(mongo, request):
        book_collection = mongo.db.books
        key = request.args.get('type')
        books = book_collection.find({'type': key})

        books_list = [book for book in books]

        for value in books_list:
            value['_id'] = str(value['_id'])
        return jsonify({'data': books_list, 'statusCode': 200})
        