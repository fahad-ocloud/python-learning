data = [
    {
        "name": "Fahad Asif",
        "age": 19,
        "city":"Lahore", 
    },
    {
        "name": "Anas Ali",
        "age": 22,
        "city":"Karachi", 
    },
    {
        "name": "Muhammad Rohan",
        "age": 21,
        "city":"Islamabad", 
    },
    {
        "name": "Muhammad Rohan",
        "age": 21,
        "city":"Islamabad", 
    },
    {
        "name": "Ayesha Khan",
        "age": 25,
        "city":"Quetta", 
    },
    {
        "name": "Hassan Ahmed",
        "age": 30,
        "city":"Lahore", 
    },
    {
        "name": "Zainab Malik",
        "age": 28,
        "city":"Faisalabad", 
    },
    {
        "name": "Usman Tariq",
        "age": 32,
        "city":"Faisalabad", 
    },
    {
        "name": "Fatima Noor",
        "age": 27,
        "city":"Hyderabad", 
    },
]

#o(n)
def group_by_func(data):
    group={}
    for value in data:
        current = value.copy()
        if group.get(value["city"]) is None:
            group.update({value["city"]:[]})
        current.pop("city")
        group[value["city"]].append(current)
    return group       
new = group_by_func(data)
print(new)