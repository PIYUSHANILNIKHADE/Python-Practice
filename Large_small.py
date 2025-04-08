arr=[1,2,3,4,5,6,7,8,6,4,3]
large=arr[0]
small=arr[0]
for i in arr:
    if i>large:
        large =i
    if i<small:
        small = i
print("Largest =",large)
print("Smallest =",small)