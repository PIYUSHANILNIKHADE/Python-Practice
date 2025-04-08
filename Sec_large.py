arr = [1,0,5,3,7,9,4,4]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("Second largest element= ",arr[1])