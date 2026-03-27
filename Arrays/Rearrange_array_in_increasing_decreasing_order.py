my_arr=[0,2,66,21,77,24,2,8]
my_arr.sort()
n=len(my_arr)
my_arr[n//2:]=reversed(my_arr[n//2:])
print(my_arr)