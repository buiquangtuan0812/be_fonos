from flask import jsonify
from bson import ObjectId
import random
import numpy as np 
import requests
from io import BytesIO
from sklearn.cluster import KMeans
import cv2

class BookController:
    @staticmethod
    def get_all_books(mongo):
        book_collection = mongo.db.books
        books = list(book_collection.find())
        books = random.sample(books, 10)
        for book in books:
            book['_id'] = str(book['_id'])

        if books is None:
            return jsonify({'message': 'Book not found', 'statusCode': 400})
        else:
            return jsonify({'data': books, 'statusCode': 200})
    @staticmethod
    def get_book_by_key(mongo, request):
        def convert_diacritics_to_regex(char):
            diacritics_map = {
                'a': '[aáàảãạăắằẳẵặâấầẩẫậ]',
                'e': '[eéèẻẽẹêếềểễệ]',
                'i': '[iíìỉĩị]',
                'o': '[oóòỏõọôốồổỗộơớờởỡợ]',
                'u': '[uúùủũụưứừửữự]',
                'y': '[yýỳỷỹỵ]'
            }
            return diacritics_map.get(char, char)
        def prepare_regex_pattern(keyword):
            return ".*" + ".*".join([convert_diacritics_to_regex(char) for char in keyword]) + ".*"
        book_collection = mongo.db.books
        key = request.args.get('key').lower()
        regex_pattern = prepare_regex_pattern(key)
        query = {'name': {'$regex': regex_pattern, '$options': 'i'}}
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
            try:
                response = requests.get(book['imgDes'])
                response.raise_for_status()  # Check for HTTP errors
                image_bytes = BytesIO(response.content)

                image = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), 1)

                image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

                pixels = image.reshape(-1, 3)

                kmeans = KMeans(n_clusters=3, n_init='auto')
                kmeans.fit(pixels)

                dominant_colors = kmeans.cluster_centers_.astype(int)

                book['_id'] = str(book['_id'])

                colors =  dominant_colors.tolist()[2]
                rgb = "rgb("
                for c in colors:
                    rgb += str(c) + ","
                rgb += "0.4)"
                return jsonify({'data': book, 'statusCode': 200, 'dominant_colors':rgb})
            except Exception as e:
                return jsonify({'message': f'Error processing image: {str(e)}', 'statusCode': 500})
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
        books_list = random.sample(books_list, len(books_list))

        for value in books_list:
            value['_id'] = str(value['_id'])
        return jsonify({'data': books_list, 'statusCode': 200})
    
    @staticmethod
    def get_book_propse_by_id(mongo, request):
        id_book = request.args.get('id')
        type_book = request.args.get('type')

        book_collection = mongo.db.books
        books = book_collection.find({'type': type_book})
        book_list = [book for book in books]

        for book in book_list:
            if (str(book['_id']) == id_book):
                book_list.remove(book)
        
        for book in book_list:
            book['_id'] = str(book['_id'])

        if (len(book_list) > 4):
            book_list = random.sample(book_list, 5)
        else :
            book_list = random.sample(book_list, len(book_list))
        
        return jsonify({'data': book_list, 'statusCode': 200})
    
    @staticmethod
    def get_book_propse_by_author(mongo, request):
        id_book = request.args.get('id')
        author = request.args.get('author')

        book_collection = mongo.db.books
        books = book_collection.find({'author': author})
        book_list = [book for book in books]

        for book in book_list:
            if (str(book['_id']) == id_book):
                book_list.remove(book)

        for book in book_list:
            book['_id'] = str(book['_id'])

        if (len(book_list) > 4):
            book_list = random.sample(book_list, 5)
        else :
            book_list = random.sample(book_list, len(book_list))

        return jsonify({'data': book_list, 'statusCode': 200})
        