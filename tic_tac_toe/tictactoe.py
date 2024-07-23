class Tictactoe:
    def __init__(self):
        self.board =[[1,2,3],[4,5,6],[7,8,9]]
    
    def add_value(self,loc,val):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == loc:
                    self.board[x][y] = val
                    return True
        return False
    def check_winner(self):
        for x in range(3):
            if self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]
            elif self.board[0][x] == self.board[1][x] == self.board[2][x]:
                return self.board[0][x]
        if self.board[0][0] ==  self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] ==  self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return False
    def game_board(self):
        row =""
        for x in range(3):
            for y in range(3):
               row += f"    {str(self.board[x][y]) if str(self.board[x][y]) =='X' or str(self.board[x][y]) =='O' else "_"}"  
            print(row)
            row=""
    def sample_board(self):
        row =""
        i=1
        for x in range(3):
            for y in range(3):
               row += f"    {i}" 
               i+=1 
            print(row)
            row=""
            