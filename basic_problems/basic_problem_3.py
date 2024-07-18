from functools import reduce
def sum_of_digit(num):
    res = [int(x) for  x in str(num)]
    if len(res) == 1:
        return res[0]
    return sum_of_digit(reduce(lambda acc, x : acc+x ,res))

print(sum_of_digit(32))