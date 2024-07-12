class Filehandling:
    def __init__(self,filename):
        self.filename = filename

    def write_to_file(self, data):
        with open(self.filename,"w") as f:
            f.write(data)
    
    def append_to_file(self, data):
        with open(self.filename ,"a") as f:
            f.write(data)
    
    def read_file(self):
        with open(self.filename , "r") as f:
            return f.read()