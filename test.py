import unittest
from main import StringCalculator

class CalcTestCase(unittest.TestCase):
    #this test case check for empty string
    def test_empty(self):
        calc = StringCalculator()
        result = calc.add("")
        self.assertEqual(result,0)

    #this test case checks string with single number
    def test_single_number(self):
        calc = StringCalculator()
        result = calc.add("1")
        self.assertEqual(result, 1)
    
    #this test case checks string with double number
    def test_double_number(self):
        calc = StringCalculator()
        result = calc.add("1,4")
        self.assertEqual(result, 5)
    
    #this test case checks string with triple number    
    def test_triple_number(self):
        calc = StringCalculator()
        result = calc.add("1,4,5,7,10,20,30")
        self.assertEqual(result, 77)
    
    #this test case checks string with alpha number
    def test_alpha_number(self):
        calc = StringCalculator()
        result = calc.add("1,2,a,c")
        self.assertEqual(result, 7)
    
    #this test case checks string with negative number
    def test_negative_number(self):
        calc = StringCalculator()
        result = calc.add("1,-2,-3,4")
        self.assertEqual(result, Exception)
    
    #this test case checks string with number that greater than 1000
    def test_greater_than_1000_number(self):
        calc = StringCalculator()
        result = calc.add("2,1002,3")
        self.assertEqual(result, 5)
    
    #this test case checks string with new line number
    def test_new_lines_number(self):
        calc = StringCalculator()
        result = calc.add("1\n2,3")
        self.assertEqual(result, 6)
    
    #this test case checks string with different delimiters number
    def test_different_delimiters_number(self):
        calc = StringCalculator()
        result = calc.add("//;\n1;2")
        self.assertEqual(result, 3)
    
if __name__ == '__main__':
    unittest.main()