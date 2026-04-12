def reversestring(s):
    return s[::-1]
def reversemethodstring(s):
    s=list(s)
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return ''.join(s)
if __name__=='__main__':
    s=input()
    print(reversestring(s))
    print(reversemethodstring(s))
