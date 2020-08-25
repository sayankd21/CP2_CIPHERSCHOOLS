def checkArmstrong(num):
    num = str(num)
    result = 0
    for digit in num:
        result += int(digit)**len(num)
    if result == int(num):
        return True
    return False

num = int(input())
print(checkArmstrong(num))
    
