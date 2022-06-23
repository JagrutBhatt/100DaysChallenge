class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        D = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        Result = 0
        for i,ele in enumerate(s):
            if i<len(s)-1:
                if D[ele] < D[s[i+1]]:
                    Result -= D[ele]
                else:
                    Result += D[ele]
            else:
                Result += D[ele]
        return Result
