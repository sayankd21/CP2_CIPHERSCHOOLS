def equilibriumIndex(lst):
    for i in range(1,len(lst)-1):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i
    return -1
    
lst = [-7, 1, 5, 2, -4, 3, 0]
print(equilibriumIndex(lst))
