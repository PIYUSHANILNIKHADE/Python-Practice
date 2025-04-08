def security_key(data):
    data_str = str(data)
    digit_count={}
    for i in data_str:
        if i in digit_count:
            digit_count[i] +=1
        else:
            digit_count[i] = 1
    key=0
    for count in digit_count.values():
        if count >1:
            key +=1
    return key

data = 5783344  23
print(security_key(data))