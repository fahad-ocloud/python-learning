arr1 = [7,1,5,2,3,6]
arr2 = [3,8,6,20,7]

def union(arr1,arr2):
    result = arr2.copy()
    for item in arr1:
        if item not in arr2:
            result.append(item)
    return result

def intersection(arr1,arr2):
    result = list()
    for item in arr1:
        if item in arr2:
            result.append(item)
    return result
def union_intersect_optimize(arr1,arr2):
    result={}
    intersect_list = []
    union_list = []
    for item in arr1:
        result[item] = result.get(item, 0)  + 1
    for item in arr2:
        result[item] = result.get(item, 0)  + 1
    for key in result:
        if result[key] >1:
            intersect_list.append(key)
        union_list.append(key)
    return f"Union : {union_list}\nIntersection : {intersect_list}"
    
        
print(union_intersect_optimize(arr1,arr2))