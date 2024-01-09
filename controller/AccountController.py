from model.Account import Account
from flask import jsonify
from flask_bcrypt import Bcrypt
from bson import ObjectId

class AccountController:
    @staticmethod
    def signup(mongo, request):
        bcrypt = Bcrypt()
        accounts = mongo.db.accounts
        account_data = request.get_json()

        account_old = accounts.find_one({'username': account_data['username']})
        if account_old:
            return jsonify({'message': 'Account already exists', 'statusCode': 409})
        else:
            email_old = accounts.find_one({'email': account_data['email']})
            if email_old:
                return jsonify({'message': 'Email already exists', 'statusCode': 409})
            else:
                password_hash = bcrypt.generate_password_hash(account_data['password'])
                new_account = Account(
                    account_data['username'], 
                    account_data['email'], 
                    password_hash, 
                    '',
                    account_data['birth_date'],
                )

                account_id = accounts.insert_one(vars(new_account))

                response = jsonify({
                    'message': 'Account added successfully', 
                    'id': str(account_id),
                    'statusCode': 200,
                })
                return response
    
    @staticmethod
    def login(mongo, request):
        bcrypt = Bcrypt()
        username  = request.get_json()['username']
        password = request.get_json()['password']

        account = mongo.db.accounts.find_one({'username': username})
        if account:
            if bcrypt.check_password_hash(account['password'], password):
                return jsonify({'message': 'Login successful', 'statusCode': 200, 'id': str(account['_id'])})
            else: 
                return jsonify({'message': 'Password incorrect', 'statusCode': 401})
        else:
            return jsonify({'message': 'Username incorrect', 'statusCode': 401})
        
    @staticmethod
    def update_profile(mongo, request):
        new_image = request.get_json()['image']
        new_birthday = request.get_json()['birthday']
        user_id = request.get_json()['user_id']

        account = mongo.db.accounts
        result = account.update_one({'_id': ObjectId(user_id)}, {'$set': {'birthday': new_birthday, 'image': new_image}})

        if result.modified_count > 0:
            return jsonify({'message': 'Updated account', 'statusCode': 200})
        else:
            return jsonify({'message': 'Update failed', 'statusCode': 401})
    
    @staticmethod
    def like_book(mongo, request):
        id_user = request.get_json()['idUser']
        id_book = request.get_json()['idBook']

        book_collection = mongo.db.books
        user_collection = mongo.db.accounts

        account = user_collection.find_one({'_id': ObjectId(id_user)})
        book = book_collection.find_one({'_id': ObjectId(id_book)})

        book_info = {}
        book_info['_id'] = str(book['_id'])
        book_info['name'] = book['name']
        book_info['imgDes'] = book['imgDes']

        favourite_books = account.get('favourite_books', [])

        favourite_books.insert(0, book_info)
        
        user_collection.update_one({'_id': ObjectId(id_user)}, {'$set': {'favourite_books': favourite_books}})
        return jsonify({'data': 'Success', 'statusCode': 200})
    
    @staticmethod
    def dislike_book(mongo, request):
        id_user = request.get_json()['idUser']
        id_book = request.get_json()['idBook']

        book_collection = mongo.db.books
        account_collection = mongo.db.accounts

        account = account_collection.find_one({'_id': ObjectId(id_user)})
        book = book_collection.find_one({'_id': ObjectId(id_book)})

        book_info = {}
        book_info['_id'] = str(book['_id'])
        book_info['name'] = book['name']
        book_info['imgDes'] = book['imgDes']

        favourite_books = account.get('favourite_books')

        favourite_books.remove(book_info)

        account_collection.update_one({'_id': ObjectId(id_user)}, {'$set': {'favourite_books': favourite_books}})

        return jsonify({'data': 'Success', 'statusCode': 200})









        