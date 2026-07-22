class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        left=0
        right=len(s)-1

        while(left<right):
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[right]==s[left]:
                right-=1
                left+=1
            else:
                return False
        return True
         