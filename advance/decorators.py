def my_decorator(func):
    def wrapper_func(*args,**kwargs):
        print("my wrapper func---")
        return func(*args,**kwargs)
    return wrapper_func
@my_decorator
def hello_World(name, place , address , age):
   return f"hellow World {name} {age} years old from {place} at {address}"

print(hello_World("fahad","lahore", "DHA",21))