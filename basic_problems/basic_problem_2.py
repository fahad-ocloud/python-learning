def decimal_to_binary(num):
    n = 0
    result=0
    while True:
        remain = num % 2
        num = int(num/2)
        result += remain*(10**n)
        if num<2:
            result+= num*(10**(n+1))
            return result
        n+=1

print(decimal_to_binary(3))

