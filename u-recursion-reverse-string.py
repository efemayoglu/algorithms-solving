def reverse(s, arr=[], index=None):
    if index == None:
        index = len(s) -1

    if index == -1:
        return ''.join(arr)

    arr.append(s[index])
    return reverse(s, arr, index-1)




def reverse2(s):
    #base case
    
    if len(s) == 1:
        return s

    #base case
    
    
    #recursion
    a =  s[len(s)-1]
    return str(a) + reverse2(s[0:len(s)-1 ])
    #recursion



def reverse3(s):

    if len(s) == 1:
        return s

    return reverse3(s[1:]) + s[0]


print(reverse3('abant'))


print(reverse('efe') == 'efe')


print(reverse2('abc') == reverse('abc',[],None))
print(reverse('hello world',[],None) == reverse2('hello world'))
