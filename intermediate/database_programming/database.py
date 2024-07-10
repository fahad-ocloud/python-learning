import sqlite3

class Person:
    
    def __init__(self,id_no=-1,first="",last="",age=-1):
        self.first = first
        self.id_no = id_no
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
       
    def load_person(self,id_no):
        self.cursor.execute(f"""
        SELECT * FROM persons WHERE id ={id_no}
        """)
        results = self.cursor.fetchone()
        self.first = results[1]
        self.id_no = id_no
        self.last = results[2]
        self.age = results[3]
    
    def __str__(self):
        return  f'id :{self.id_no} first :{self.first} last : {self.last} age : {self.age}'


p1 = Person()
p1.load_person(3)
print(p1)
# connection = sqlite3.connect('mydata.db')
# cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER    
# )
# """)
# cursor.execute("""
# INSERT INTO persons VALUES 
# (1,'Fahad','Asif', 21),
# (2,'Moiz','Asif', 11),
# (3,'Ali','Asif', 41),
# (4,'Ahmed','Asif', 31)
# """)


# rows  = cursor.fetchall()
# print(rows)
# connection.commit()
# connection.close()