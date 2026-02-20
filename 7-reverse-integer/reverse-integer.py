class Solution(object):
    def reverse(self, x):
        dig=0
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        while(x>0):
            res=x%10
            dig=dig*10+res
            x=x//10
        result=sign*dig
        if result<-2**31 or result > 2**31 -1:
            return 0
        return result
        