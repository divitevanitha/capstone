import calc
import unittest
class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15),25)
        self.assertEqual(calc.add(10.22, 15.31), 25.53)
    def test_sub(self):
        self.assertEqual(calc.sub(10, 15), -5)
        self.assertEqual(calc.sub(10.22, 15.31), -5.09)
    def test_mul(self):
        self.assertEqual(calc.mul(10, 15), 150)
        self.assertEqual(calc.mul(2.00, 3.00), 6.00)
    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)

if __name__ == "__main__":
    unittest.main()
