def count_down(n):
    while not n==0:
        yield n
        n-=1

n = count_down(10)  
for i in n:
    print(i)
