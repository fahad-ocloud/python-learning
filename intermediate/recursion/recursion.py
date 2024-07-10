def power_of_func(number, power):
    if power == 0:
        return 1
    return number * power_of_func(number,power-1) 

def fibonacci(number):
    if(number<=1):
        return number
    return fibonacci(number-1) +fibonacci(number-2)
    
print(fibonacci(3))
print(power_of_func(10,3))