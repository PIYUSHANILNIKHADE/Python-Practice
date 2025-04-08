x=int(input("Enter a number"))
a=0
n=len(str(x))
for digit in str(x):
    a += int(digit) ** n
if x==a:
    print("It's Armstrong number")
else:
    print("It's not an armstong number")