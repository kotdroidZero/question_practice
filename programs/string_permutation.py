def findAllPermu(s):
    permutations = set()
    for char in s:
        val = recur(char, s.replace(char, ""))
        permutations.add(val)
    print(permutations)


def recur(s1, s2):
    if len(s1) == 1:
        return s2+s1
    else:
        recur(s1[0], s2[1, len(s2-1)])


ab = set()
ab.add('d')
print(ab)
findAllPermu("mari")
