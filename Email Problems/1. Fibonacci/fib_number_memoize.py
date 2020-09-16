#import unittest


class Fibber(object):
    def __init__(self):
        self.memo = {}
    
    def fib(self, n):
        if n < 0:
            # Edge case: negative index
            raise ValueError('Index was negative. No such thing as a negative'
                            'index in a series...')
        if n in [0, 1]:
            # Base case: 0 or 1
            return n
        
        # See if we have already calculated this 
        if n in self.memo:
            return self.memo[n]
        
        result = self.fib(n-1) + self.fib(n-2)

        # Memoize
        self.memo[n] = result

        return result   

print("Fib : ")
fibaaaaaaa = Fibber()
print(fibaaaaaaa)
print(fibaaaaaaa.fib(7))
