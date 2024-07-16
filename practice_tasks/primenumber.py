def is_prime(n):
    if n<=1:
        return False
    for x in range(2,int(n**0.5)+1):
        if n%x ==0:
            return False
    return True

print(is_prime(9))