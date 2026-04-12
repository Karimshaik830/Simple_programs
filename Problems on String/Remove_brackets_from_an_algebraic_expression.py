def removealgebra(s):
    result=[]
    for ch in s:
        if ch not in '()':
            result.append(ch)
    return ' '.join(result)
if __name__=='__main__':
    s=input()
    print(removealgebra(s))
