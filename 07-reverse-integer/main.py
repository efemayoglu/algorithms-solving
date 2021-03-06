import sys
class Solution:
    def reverse(self, x: int) -> int:
        if self.isValidInteger(x) == False:
            return 0

        newInt = 0
        lenOfX =len(str(x))
        lenOfX = lenOfX -1 if x <0 else lenOfX
        factor = int(pow(10, (lenOfX -1)))
        factor = factor * -1 if x<0 else factor
        if lenOfX == 1:
            return x
        try:
            if x>=9:
                while x>=9:
                    lastDigit = x%10
                    newInt = newInt+ (lastDigit * factor)
                    x = int(x/10)
                    factor = int(factor / 10)
                newInt += x
            elif x<=-9:
                while x <=-9:
                    lastDigit = abs(x)%10
                    newInt = newInt+ (lastDigit * factor)
                    x = int(x/10)
                    factor = int(factor / 10)
                newInt += x

            if self.isValidInteger(newInt) == False:
                return 0
            return newInt

        except:
            return 0
    def isValidInteger(self, x):
        if x <= -pow(2,31) or x>= (pow(2,31)-1):
            return False
        return True
