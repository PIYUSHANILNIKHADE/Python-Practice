num = int(input('Enter Number'))
result=''
digits='0123456789'
while num !=0:
    result = result + digits[num % 10]
    num = num // 10
print(result)
print(type(result))