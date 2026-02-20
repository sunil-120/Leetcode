class Solution(object):
    def isValid(self, s):
        stack=[]
        mapp={"[":"]","{":"}","(":")"}
        for i in s:
            if i in mapp:
                stack.append(i)
            elif i in mapp.values():
                if not stack or mapp[stack[-1]]!=i:
                    return False
                stack.pop()
            else:
                return False
        return not stack
        