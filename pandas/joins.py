import pandas as pd


names= {
    'SSN':[2,3,4,5,6],
    'Name':["Anna","Ahmad","Ali","Rohan","Fahad"]
}

ages={
    'SSN':[1,2,3,4],
    'Age':[23,24,25,77]
}

d1 = pd.DataFrame(names)
d2 = pd.DataFrame(ages)

df = pd.merge(d1,d2,on='SSN',how='outer')
df.set_index('SSN',inplace=True)

print(df)

