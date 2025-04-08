import collections
def sumoddintegers(arrr,n):

    mp = collections.defaultdict(int)
    for i in range(n):
        mp[arr[i]] += 1
    sum=0

    for i in mp:
        if(mp[i] % 2!=0):
