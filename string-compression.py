def compress(s):
    index = 0
    lastChar = s[0]
    n = ""

    while index < len(s):  
        counter = 0
        
        while index < len(s) and s[index] == lastChar:
            counter += 1
            index += 1

        n += f'{lastChar}{counter}'

        if index < len(s):
            lastChar = s[index]

    return n

#manuel debugging
            #AAAAABBBBCCCC
#counter=0, index=0, lastChar=A, s[index]= A
#counter=1, index=1, lastChar=A, s[index]= A
#counter=2, index=2, lastChar=A, s[index]= A
#counter=3, index=3, lastChar=A, s[index]= A
#counter=4, index=4, lastChar=A, s[index]= A,


print( compress('AAAAABBBBCCCC') )

print( compress('AAAAABBBBCCCC') ==   'A5B4C4')


# String Compression
# Problem¶
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.