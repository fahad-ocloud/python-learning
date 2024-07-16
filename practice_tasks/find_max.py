def find_max(a,b,c):
    arr=[a,b,c]
    min=0
    for i in arr:
        if min < i:
            arr.remove(i)
            return arr
def first_two_max(a, b, c):
    numbers = [a, b, c]
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1, max2

print(find_max(2,3,5))
print(first_two_max(2,4,7))