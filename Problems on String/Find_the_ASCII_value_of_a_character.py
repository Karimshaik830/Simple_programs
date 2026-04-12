s='A'
print(ord(s))


s='karim'
ascii_value=[]
for i in s:
    ascii_value.append(ord(i))
print(ascii_value)
print(*ascii_value)

sum=0
for i in ascii_value:
    sum+=i
print(sum)