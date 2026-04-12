def sumofnumbers(s):
    sum=0
    temp=""
    for ch in s:
        if ch.isdigit():
            temp+=ch
        else:
            if temp!="":
                sum+=int(temp)
                temp=""
    if temp!="":
        sum+=int(temp)

    return sum
if __name__=="__main__":
    s=input()
    print(sumofnumbers(s))
