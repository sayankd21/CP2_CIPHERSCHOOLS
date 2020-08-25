a = [ 1, 2, 3 ]
b = [ 2, 1, 4 ]
a.reverse()
b.reverse()
result1 = result2 = 0
for index,digit in enumerate(a):
    result1 += digit * 10**index
for index,digit in enumerate(b):
    result2 += digit * 10**index
print(result1 + result2)

    
