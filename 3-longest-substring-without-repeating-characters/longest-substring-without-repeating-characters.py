class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=[]
        for j in range(len(s)):
            lst=[]

            for i in range(j,len(s)):
                if s[i] in lst:
                    break
                else:
                    lst.append(s[i])
            if len(a)<len(lst):
                a=lst
        return len(a)
