class Solution(object):
    def romanToInt(self, s):
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        n=len(s)
        for i in range(n):
            if i<n-1 and rom[s[i]]<rom[s[i+1]]:
                total-=rom[s[i]]
            else:
                total+=rom[s[i]]
        return total
            
        