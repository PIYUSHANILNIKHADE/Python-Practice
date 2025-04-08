s =input("Enter string")
flag=True
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
        flag=False
        print("Not Palindrome")
        break
print("It's palindrome")