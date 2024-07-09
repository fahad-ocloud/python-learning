buyer_credit= True
price = 1000000
if buyer_credit:
    down_payment= price * 0.1
else:
    down_payment= price * 0.2
print(down_payment)

weight = input("Enter your weight : ")
type_of_weight = input("kg(k) or lbs(l) : ")

if type_of_weight.lower() =='k':
    print(int(weight)/0.45)
elif type_of_weight.lower() == 'l':
    print(int(weight)*0.45)
else:
    print("invalid input")