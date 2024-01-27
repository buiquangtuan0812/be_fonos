import datetime

class Comment:
    def __init__(self, content, user, book, rating):
        self.content = content
        self.user = user
        self.book = book
        self.rating = rating
        self.like = 0
        self.interact = []
        self.timestamp = datetime.datetime.now()
