my_arr=[12,44,67,89,221,678]
my_val=my_arr[0]
sec_small=float('inf')
sec_high=float('inf')
for i in my_arr:
    if i<my_val:
        sec_small=my_val
        my_val=i
    elif i<sec_small and i!=my_val:
        sec_small=i
print(sec_small)
for j in my_arr:
    if j>my_val:
        sec_high=my_val
        my_val=j
    elif j>sec_high and j!=my_val:
        sec_high=j
print(sec_high)