def isPalindrome(s):
    newStr=''
    print(len(s))
    for i in range(len(s)-1,-1,-1):
        newStr=newStr+s[i]
    return newStr.lower() == s.lower()
st = "Ababa"
isP = isPalindrome(st)
print("{} is palindrome ? {}".format(st,isP))