def isAnagram(s1,s2):

    print(s1)
    print(s2)

    letterCount = {}
    if len(s1) !=  len(s2):
        return False
    else:
        for char in s1.lower():
            if char not in letterCount:
                letterCount[char]=1
            else:
                letterCount[char]=letterCount[char]+1

        print(letterCount)

        for char2 in s2.lower():
            if char2 in letterCount and letterCount[char2] != 0:
                letterCount[char2]=letterCount[char2]-1
                if letterCount[char2]==0:
                    letterCount.pop(char2)


        return len(letterCount)==0      


anagram= isAnagram("pushkar","PushKRA")  
print(anagram)