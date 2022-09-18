class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #recursive approach call n//2 until n==1 or -1
        
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        
        result = self.myPow(x,n//2)
        
        return result*result*(x if n % 2 else 1)