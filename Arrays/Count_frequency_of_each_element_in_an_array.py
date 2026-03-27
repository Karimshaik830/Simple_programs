from collections import Counter
my_arr=[1,2,3,4,12,34,1,2,3,4]
frequency={}
for i in my_arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)


count=Counter(frequency)
print(count)