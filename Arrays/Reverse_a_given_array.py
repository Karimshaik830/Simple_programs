my_arr=[9,8,7,6,5,4,3,2,1]
my_arr[:]=my_arr[::-1]
print(my_arr)

left=0
right=len(my_arr)-1
while left<right:
    my_arr[left],my_arr[right]=my_arr[right],my_arr[left]
    left+=1
    right-=1
print(my_arr)

my_arr.reverse()
print(my_arr)