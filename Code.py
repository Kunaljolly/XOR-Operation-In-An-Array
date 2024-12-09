class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        t = [(start+(2*x)) for x in range(n)]
        xor = t[0]
        for x in range(1,len(t)):
            xor = t[x]^xor
        return xor
            
