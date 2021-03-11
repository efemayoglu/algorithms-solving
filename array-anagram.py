def anagram(s1,s2):
    a = {}
    for i in s1:
        if i not in a:
            if i != ' ':
                a[i] = 1
        else:
            a[i] += 1
            
    for i in s2:
        if i != ' ':
            if i in a:
                if a[i] > 0:
                    a[i] = a[i] -1
                else:
                    return False
            else:
                return False

    for i in a.keys():
        if a[i] != 0:
            return False

    return True
            
            
print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('public relations','crap built on lies'))




#def anagram(s1, s2):
    #s1 = s1.replace(' ','').lower()
    #s2 = s2.replace(' ','').lower()
    #return sorted(s1) == sorted(s2)
