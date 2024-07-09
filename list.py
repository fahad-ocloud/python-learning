# program to fine largest number from list
list1 =[1,3,4,6,2,7,8]
max=0
for item in list1:
    if(item>max):
        max=item
print(f'Largest number is {max}')

# remove duplicates in list
lists = [1,2,3,4,2,3,4,6,8,9,1,3,6]
newList=[]
for item in lists:
   if(item not in newList):
       newList.append(item)
print(newList)