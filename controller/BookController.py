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
            return jsonify({"message": "No books found"}), 400
        else:
            return books, 200
        
    @staticmethod
    def get_book_by_key(mongo, request):
        book_collection = mongo.db.books
        key = request.args.get('key')
        query = {'name': {'$regex': key, '$options': 'i'}}
        books = list(book_collection.find(query))
        for book in books:
            book['_id'] = str(book['_id'])

        if books is None:
            return jsonify({'message': 'Book not found'}), 404
        else:
            return books, 200
            
    
    @staticmethod
    def get_book_by_id(mongo, request):
        book_collection = mongo.db.books
        id_book = request.args.get('id')
        object_id = ObjectId(id_book)
        book = book_collection.find_one({'_id': object_id})

        if book is not None:
            book['_id'] = str(book['_id'])
            return book, 200
        else:
            return jsonify({'message': 'Book not found'}), 404
    
    @staticmethod
    def get_book_propose(mongo):
        book_collection = mongo.db.books
        books = list(book_collection.find())
        book = random.sample(books, 8)
        for value in book:
            value['_id'] = str(value['_id'])
        return book, 200
        