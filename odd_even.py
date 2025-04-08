
Start=int(input("Enter a starting of range"))
end=int(input("Enter a ending of range"))

odd_no = []
even_no = []
for i in range (Start,end+1):
    if i%2 ==0 :
        even_no.append(i)
    else:
        odd_no.append(i)
print("Odd Numbers:",odd_no)
print("Even Numbers:",even_no)