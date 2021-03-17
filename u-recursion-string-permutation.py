def permute(s):
    
    out = []

    
    #Base Case
    if len(s) == 1:
        out = [s]

    else:

        #for every letter in string 

        for i,let in enumerate(s):

            # For every permutation resulting from Step 2 and 3

            for perm in permute(s[:i]+ s[i+1:]):
               print(f'perm is {perm}')
               out += [let+perm]
               print(f'out = {out}')

    return out





print(permute('abc'))
print(permute('abcd'))
print(len(permute('abcd')))
#
