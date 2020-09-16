#sys.path.append(".")
# Not able to intergrate with its class for this test!
# Was Able to after a stupid class object creation in every test function call

from fib_number_memoize import *
import unittest

# Tests
class Test(unittest.TestCase):
    fi = Fibber() # i was not able to make it use in the below defination so labor work done below
    def test_zeroth_fibonacci(self):    
        fi = Fibber()    
        actual = fi.fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        fi = Fibber()
        actual = fi.fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        fi = Fibber()
        actual = fi.fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        fi = Fibber()
        actual = fi.fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        fi = Fibber()
        actual = fi.fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        fi = Fibber()
        actual = fi.fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2) 