def removecons(s):
    vowels=set('aeiouAEIOU')
    result=[]
    for ch in s:
        if ch in vowels or not ch.isalpha():
            result.append(ch)
    return ''.join(result)
if __name__=='__main__':
    s=input()
    print(removecons(s))