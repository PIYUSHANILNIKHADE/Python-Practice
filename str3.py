#Convert string into title without using title funtion
s = input('Enter string')
x=[]
for i in s.split():
    x.append(i[0].upper() + i[1:].lower())
print(' '.join(x))
