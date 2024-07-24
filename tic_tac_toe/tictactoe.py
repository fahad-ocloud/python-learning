class Tictactoe:
    def __init__(self,size):
        self.board =[[(i * size + j + 1) for j in range(size)] for i in range(size)]
        self.size = size
    def add_value(self,loc,val):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == loc:
                    self.board[x][y] = val
                    return True
        return False
    # def check_winner(self):
    #     for x in range(3):
    #         if self.board[x][0] == self.board[x][1] == self.board[x][2]:
    #             return self.board[x][0]
    #         elif self.board[0][x] == self.board[1][x] == self.board[2][x]:
    #             return self.board[0][x]
    #     if self.board[0][0] ==  self.board[1][1] == self.board[2][2]:
    #         return self.board[0][0]
    #     if self.board[0][2] ==  self.board[1][1] == self.board[2][0]:
    #         return self.board[0][2]
    #     return False
    
    
    def check_winner(self,val):
        
        for row in range(self.size):
            count = 0
            for col in range(self.size):
                if val == self.board[row][col]:
                    count+=1
                    if count==self.size:
                       return val
                else:
                    count=0
        for col in range(self.size):
            count = 0
            for row in range(self.size):
                if val == self.board[row][col]:
                    count+=1
                    if count==self.size:
                       return val
                else:
                    count=0
        d_count = 0
        for diag in range(self.size):
            if self.board[diag][diag] == val:
                d_count+=1  
                print(count)
            else:
                d_count=0
        if d_count==self.size:
                return val
        for diag in range(self.size):
            if self.board[diag][self.size-diag-1] == val:
               d_count+=1  
            else:
               d_count=0
        if d_count==self.size:
                return val
        return False
            
    def game_board(self):
        row =""
        for x in range(self.size):
            for y in range(self.size):
               row += f"    {str(self.board[x][y]) if str(self.board[x][y]) =='X' or str(self.board[x][y]) =='O' else "_"}"  
            print(row)
            row=""
    def sample_board(self):
        row =""
        i=1
        for x in range(self.size):
            for y in range(self.size):
               row += f"    {i}" 
               i+=1 
            print(row)
            row=""
            