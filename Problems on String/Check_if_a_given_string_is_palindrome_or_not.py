def palindrome(i,s):
    if i>=len(s)-1:
        return True
    if s[i]!=s[len(s)-1-i]:
        return False
    return palindrome(i+1,s)
if __name__=="__main__":
    s=input()
    print(palindrome(0,s))