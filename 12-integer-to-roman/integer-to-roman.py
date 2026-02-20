class Solution(object):
    def intToRoman(self, num):
        iin = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]
        tot=""
        for i in range(len(sym)):
            while num>=iin[i]:
                tot+=sym[i]
                num-=iin[i]
        return tot
                
        