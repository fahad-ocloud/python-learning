from datetime import datetime
class Book:
    def __init__(self,title,content,author,updated):
        self.title = title
        self.content = content
        self.author = author
        # self.quantity = quantity
        # self.assign = assign
        if updated:
            self.createdAt= updated
        else:
            self.createdAt=datetime.now()
        self.updatedAt = datetime.now()
        