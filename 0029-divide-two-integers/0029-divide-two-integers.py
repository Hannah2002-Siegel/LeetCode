class Solution(object):
    def divide(self, dividend, divisor):
        if dividend*divisor>0:
            res=abs(dividend)//abs(divisor)
        else:
            res=-(abs(dividend)//abs(divisor))
        intmin=-(2**31)
        intmax=(2**31)-1
        return res if intmin<=res<=intmax else intmax
        