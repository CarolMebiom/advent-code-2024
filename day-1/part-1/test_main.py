import unittest
from main import split_numbers, select_small_number

class TestMain(unittest.TestCase):
    def test_split_numbers(self):
        a = []
        b = []
        input = ['1 2\n', '3 4\n']
        split_numbers(input, a, b)
        self.assertEqual(a, [1, 3])
        self.assertEqual(b, [2, 4])
    
    def test_split_numbers_empty_input(self):
        a = []
        b = []
        input = []
        split_numbers(input, a, b)
        self.assertEqual(a, [])
        self.assertEqual(b, [])

    def test_split_numbers_lists(self):
        a = 2
        b = 'a'
        input = {'a': 'b'}
        input_correct = ['1 2\n', '3 4\n']
        self.assertRaises(KeyError, split_numbers, input, a, b)
        self.assertRaises(AttributeError, split_numbers, input_correct, a, b)
    
    def test_select_small_number(self):
        a = [1, 2, 3]
        b = [10, 5, 8]
        self.assertEqual(select_small_number(a), 1)
        self.assertEqual(select_small_number(b), 5)
        self.assertEqual(a, [2, 3])
        self.assertEqual(b, [10, 8])
    
    def test_select_small_number_empty_list(self):
        a = []
        self.assertRaises(ValueError, select_small_number, a)
    
    def test_select_small_number_type_error(self):
        a = 'a'
        self.assertRaises(AttributeError, select_small_number, a)
    

if __name__ == "__main__":
    unittest.main()