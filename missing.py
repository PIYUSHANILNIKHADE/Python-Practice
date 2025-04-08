
arr = list(map(int,input("Enter array= ").split(',')))
N=int(input("Enter length of array= "))
missing_found = False

for i in range(1,N+1):
    if i not in arr:
        print("Missing number= ", i)
        missing_found = True
if not missing_found:
    print("No missing number")