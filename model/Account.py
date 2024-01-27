import datetime

class Account:
    def __init__(self, username, email, password, image, birthday):
        self.username = username
        self.email = email
        self.password = password
        self.image = image
        self.birthday = birthday
        self.timestamp = datetime.datetime.now()