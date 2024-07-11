def my_func(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])
    print(kwargs['KEYONE'])
my_func(1,2,3,4,5,KEYONE=9)