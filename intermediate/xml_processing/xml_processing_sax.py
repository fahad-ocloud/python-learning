from xml import sax

class GroupHandler(sax.ContentHandler):
    def startElement(self,name, attrs):
        self.current = name
        if self.current =='person':
            print('-----PERSON-------')
            print(f'ID : {attrs['id']}')
    
    def characters(self,content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'age':
            self.age = content
        elif self.current == 'weight':
            self.weight = content
        elif self.current == 'height':
            self.height = content
    def endElement(self,name):
        if self.current == 'name':
            print(f'name : {self.name}')
        elif self.current == 'age':
            print(f'age : {self.age}')
        elif self.current == 'weight':
            print(f'weight : {self.weight}')
        elif self.current == 'height':
            print(f'height : {self.height}')
        self.current = ""

handler = GroupHandler()
parser = sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')