from model.Account import Account
from flask import jsonify
from flask_bcrypt import Bcrypt

class AccountController:
    @staticmethod
    def signup(mongo, request):
        bcrypt = Bcrypt()
        accounts = mongo.db.accounts
        account_data = request.get_json()

        account_old = accounts.find_one({'username': account_data['username']})
        if account_old:
            return jsonify({'message': 'Account already exists'}), 409
        else:
            email_old = accounts.find_one({'email': account_data['email']})
            if email_old:
                return jsonify({'message': 'Email already exists'}), 409
            else:
                password_hash = bcrypt.generate_password_hash(account_data['password'])
                new_account = Account(
                    account_data['username'], 
                    account_data['email'], 
                    password_hash, 
                    ''
                )

                account_id = accounts.insert_one(vars(new_account))

                response = jsonify({
                    'message': 'Account added successfully', 
                    'id': str(account_id)
                })
                response.status_code = 200
                return response
    
    @staticmethod
    def login(mongo, request):
        bcrypt = Bcrypt()
        username  = request.get_json()['username']
        password = request.get_json()['password']

        account = mongo.db.accounts.find_one({'username': username})
        if account:
            if bcrypt.check_password_hash(account['password'], password):
                return jsonify({'message': 'Login successful'}), 200
            else: 
                return jsonify({'message': 'Password incorrect'}), 401
        else:
            return jsonify({'message': 'Username incorrect'}), 401