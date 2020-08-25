def isMirrorInverse(arr, n) : 
    for i in range(n) :  
        if (arr[arr[i]] != i) : 
            return False  
    return true
    
arr = [ 1, 2, 3, 0 ] 
n = len(arr):
if (isMirrorInverse(arr,n)): 
  print("Yes")
else:
  print("No")
