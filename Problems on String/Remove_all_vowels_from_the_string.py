def removeVowle(s)->str:
    vowel=set('aeiouAEIOU')
    result=[]
    for ch in s:
        if ch not in vowel:
            result.append(ch)
    return ''.join(result)
if __name__=='__main__':
    s=input()
    print(removeVowle(s))