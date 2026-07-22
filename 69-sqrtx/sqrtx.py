class Solution(object):
    def mySqrt(self, x):
        ans=0
        if x==0:
            return x

        left=1
        right=x
        while(left<=right):
            mid = (left+right)/2
            if (mid*mid==x):
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                ans=mid
                left=mid+1
        return ans
