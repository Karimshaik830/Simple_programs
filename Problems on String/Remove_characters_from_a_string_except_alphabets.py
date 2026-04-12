def removealphabet(s):
    result=[]
    for ch in s:
        if 'a'<=ch<='z' or 'A'<=ch<='Z':
            result.append(ch)
    return ''.join(result)
if __name__=='__main__':
    s=input()
    print(removealphabet(s))