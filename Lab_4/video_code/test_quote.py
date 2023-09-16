""" Create unit testing. """

import unittest
from unittest import TestCase

import quote # importing quote.py

class QuoteTest(TestCase):

    def test_quote_for_small_lawn_for_same_day(self): # def a test function
        actual_quote = quote.lawn_quote('small', True) # call lawn_quote and pass two arguments
        expected_quote = 15 # expected value base on arguments passed to lawn_quote()
        self.assertEqual(expected_quote, actual_quote) # best to pass expected_quote first and actual_quote second

    #def second test function
    def test_quote_for_large_lawn_not_same_day(self): # def a test function
        actual_quote = quote.lawn_quote('large', False) # call lawn_quote and pass two arguments
        expected_quote = 20 # expected value base on arguments passed to lawn_quote()
        self.assertEqual(expected_quote, actual_quote)

    #def third test function, validator
    def test_quote_for_unrecognized_sizes(self): # def a test function
        actual_quote = quote.lawn_quote('grande', False) # call lawn_quote and pass two arguments
        self.assertIsNone(actual_quote) 

        # Longer version below:
        # expected_quote = None # expected value base on arguments passed to lawn_quote()
        # self.assertEqual(expected_quote, actual_quote)

if __name__ == '__main__':
    unittest.main()