
n=9
arr=[10,12,5,40,30,7,5,9,10]
j=0
for i in range(n):
    if arr[i]%10 !=0 :
        arr[i],arr[j] = arr[j],arr[i]
        j+=1
print(arr)