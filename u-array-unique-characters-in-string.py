#python trick 1line 
# def uni_char(s):
#     return len(set(s))  == len(s)


def uni_char(s):
    a = {}

    for i in s:
        if i in a:
            return False
        else:
            a[i] = True

    return True





print(uni_char('abcdefg') ==  True)
print(uni_char('goo') ==  False)
print(uni_char('abcdefg') ==  True)



# """
# RUN THIS CELL TO TEST YOUR CODE>
# """
# from nose.tools import assert_equal


# class TestUnique(object):

#     def test(self, sol):
#         assert_equal(sol(''), True)
#         assert_equal(sol('goo'), False)
#         assert_equal(sol('abcdefg'), True)
#         print 'ALL TEST CASES PASSED'
        
# # Run Tests
# t = TestUnique()
# t.test(uni_char)





# Unique Characters in String
# Problem
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

# Solution
# Fill out your solution below: