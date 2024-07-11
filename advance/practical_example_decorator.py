import time

def logged(func):
    def wrapper(*args,**kwargs):
        value= func(*args,**kwargs)
        with open("logFile.txt","a+") as f:
            fname= func.__name__
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper



def timed(func):
    def wrapper(*args,**kwargs):
        before = time.time()
        value  = func(*args,**kwargs)
        after = time.time()
        fname = func.__name__
        print(f"{fname} took {after-before} sec to execute the function !")
        return value

    return wrapper
# @logged
@timed
def add(x,y):
    return x+y
print(add(30,10))