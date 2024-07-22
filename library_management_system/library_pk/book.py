from datetime import datetime
class Book:
    def __init__(self,title,content,author,createdAt,updatedAt):
        self.title = title
        self.content = content
        self.author = author
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.isAvailable = True
        self.borrowed_name :str = ""
        self.borrower_email:str = ""
