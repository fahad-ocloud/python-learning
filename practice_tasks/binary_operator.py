def binary_operator(a,b):
    and_opt = a and b
    or_opt = a or b
    xor_opt = a ^ b
    return and_opt, or_opt , xor_opt

print(binary_operator(7,7))
    
    