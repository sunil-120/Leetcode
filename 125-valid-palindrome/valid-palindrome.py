class Solution(object):
    def isPalindrome(self, s):
        found = True
        s=s.lower()
        left=0
        right=len(s)-1

        while(left<right):
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left]==s[right]:
                        right-=1
                        left+=1 
                    else:
                        found=False
                        break
                else:
                    right-=1   
            else:
                left+=1
        return found