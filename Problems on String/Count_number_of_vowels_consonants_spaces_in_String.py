def count(s):
    vowels=0
    cons=0
    spaces=0
    s=s.lower()
    for ch in s:
        if ch in'aeiou':
            vowels+=1
        elif 'a'<=ch<='z':
            cons+=1
        elif ch==' ':
            spaces+=1
    print(vowels,cons,spaces)

if __name__=='__main__':
    s=input()
    count(s)