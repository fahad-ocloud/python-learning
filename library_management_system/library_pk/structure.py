import struct
from datetime import datetime
from .book import Book
class Structure:
    def __init__(self):
        self.format ='50s 200s 50s Q Q ? 50s 50s'
    def serialize_data(self,book:Book):
        packed_data = struct.pack(
        self.format,
        book.title.encode().ljust(50, b'\0'),  
        book.content.encode().ljust(200, b'\0'), 
        book.author.encode().ljust(50, b'\0'),  
        int(book.createdAt.timestamp()),  
        int(book.updatedAt.timestamp()),
        book.isAvailable,
        book.borrowed_name.encode().ljust(50, b'\0'),   
        book.borrower_email.encode().ljust(50, b'\0'),   
        )
        return packed_data
    def deserialize_data(self,data):
        if not isinstance(data, bytes):
            raise ValueError("Expected bytes-like object for deserialization")
        unpacked_data = struct.unpack(self.format, data)
        title = unpacked_data[0].decode().strip('\0')
        content = unpacked_data[1].decode().strip('\0')
        author = unpacked_data[2].decode().strip('\0')
        createdAt = datetime.fromtimestamp(unpacked_data[3])
        updatedAt = datetime.fromtimestamp(unpacked_data[4])
        book = Book(title,  content,  author,   createdAt,    updatedAt )
        book.isAvailable = unpacked_data[5]
        book.borrowed_name = unpacked_data[6].decode().strip('\0')
        book.borrower_email = unpacked_data[7].decode().strip('\0')
        return book 
    def cal_size(self):
        return struct.calcsize(self.format)