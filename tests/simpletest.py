import unittest   # The test framework
from database import salesprocessor

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(salesprocessor.increment(4), 5)

  

if __name__ == '__main__':
    unittest.main()