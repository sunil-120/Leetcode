class Solution(object):
    def isPalindrome(self, x):
        n=x
        digit=0
        while(n>0):
            res=n%10
            digit=digit*10+res
            n=n//10
        return x==digit 