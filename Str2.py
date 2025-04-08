s=input('enter string')
l=[]
temp =''
for i in s:
    if i != '':
        temp +=i
    else:
        l.append(temp)
        temp=''
l.append(temp)
print(l)
