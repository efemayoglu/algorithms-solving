def rev_word(s):

    whiteSpaceIndex = 0
    whiteSpaceIndex2 = len(s) -1


    #delete space from while found a char except 'space'
    while s[whiteSpaceIndex] == ' ':
        whiteSpaceIndex+=1

    #delete space start end from while found a char except 'space'
    while s[whiteSpaceIndex2] == ' ':
        whiteSpaceIndex2-=1

    a = []
    startPosition = whiteSpaceIndex
    
    # for i in range(whiteSpaceIndex, whiteSpaceIndex2):
    i = whiteSpaceIndex

    while i >= whiteSpaceIndex and i<=whiteSpaceIndex2:
        if s[i] == ' ':
            x = i + 1

            #if there are multi space in the middle of the sentence jump up while != space
            while s[x] == ' ':
                x+=1
            
            a.append(s[startPosition:i])#add to array 
            i = x -1
            startPosition = i + 1
        
        i+=1 #everytime index+=1

    a.append(s[startPosition: whiteSpaceIndex2+1])

    b = []
    for i in range(len(a)):   #abc fgd
        b.append(
            a[len(a) -1 - i]
         )

    return ' '.join(b)




print (rev_word('Hi John,   are you ready to go?') == 'go? to ready you are John, Hi')


print (rev_word('    space before') == 'before space')




# Sentence Reversal
# Problem
# Given a string of words, reverse all the words. For example:

# Given:

# 'This is the best'
# Return:

# 'best the is This'
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

# '  space here'  and 'space here      '
# both become:

# 'here space'