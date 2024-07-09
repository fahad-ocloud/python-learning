from functools import reduce

# def suming(a,b):
#     return a+b

# sum_of_number = partial(suming,b=3)

# print(sum_of_number(6))
# fancy_camp = {x:(lambda x: x*x)(x) for x in range(5)}
# print(fancy_camp)



lists = [1,3,52,35,6,88,9,9]

value  = reduce(lambda acc,x: acc+x  ,lists)
print(value)
