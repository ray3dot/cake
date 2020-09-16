import unittest


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

# Can define the class here?
class Test(unittest.TestCase):
    #fi = Fibber() # i was not able to make it use in the below defination so labor work done below
    def test_zeroth_fibonacci(self):    
        #fi = Fibber()    
        #actual = fi.fib(0)
        actual = fibaaaaaaa.fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        #fi = Fibber()
        actual = fibaaaaaaa.fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        fi = Fibber()
        actual = fibaaaaaaa.fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        fi = Fibber()
        actual = fibaaaaaaa.fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        fi = Fibber()
        actual = fibaaaaaaa.fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        fi = Fibber()
        actual = fibaaaaaaa.fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2) 
