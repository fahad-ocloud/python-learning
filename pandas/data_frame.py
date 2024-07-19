import pandas as pd

data = {
    "Name":["Fahad","Ahmad","Ali","Rohan"],
    "Age":[21,21,31,42],
    "Height":[143,132,122,111],
    "Gender":["m","m","m","m"]
}

df = pd.DataFrame(data)

print(df)
print(df['Name'].iloc[1])

print(df['Age'].prod())
print(df['Age'].mean())
print(df.describe())
print(f"median : {df['Age'].median()}")