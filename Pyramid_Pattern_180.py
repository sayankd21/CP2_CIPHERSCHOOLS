n = int(input())
i = 0
for i in range(n):
    for _ in range(i+1, n):
        print(" ", end = " ")
    for _ in range(i+1):
        print("*", end = " ")
    print("")
