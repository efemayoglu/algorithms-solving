def rec_sum(n):
        if n==0:
            return 0
        return n + rec_sum(n-1)


print(rec_sum(4) == 10)

print(rec_sum(5) == 15)



def sum_func(n):
    if n < 10:
        return n
    
    return n%10 + sum_func(n//10)


print(sum_func(4321)==10)

print(sum_func(1234)==10)

print(sum_func(8789)==32)


def word_split(phrase, list_of_words, output  = None):

    if output == None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output



print(word_split('themanran', ['crown','man','ran']))

print(word_split('themanran',['man','the','ran']))
