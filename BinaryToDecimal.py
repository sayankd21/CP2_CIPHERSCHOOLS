def binaryToDecimal(num):
    i = 0
    result = 0
    while num != 0:
        n = num % 10
        result += n * 2**i
        i += 1
        num = num//10
    return result
binary = int(input())
print(binaryToDecimal(binary))
        
    
    
