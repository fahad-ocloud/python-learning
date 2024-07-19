import pandas as pd

def cube_func(a):
    return a * a * a
series = pd.Series([1,2,3,4,5,6],["a","b","c","d","e","f"])

print(series)
print(series.apply(cube_func))