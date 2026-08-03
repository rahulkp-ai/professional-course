import unittest

from mymodule import square,add

class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2),4)
    
    def test_add(self):
        self.assertEqual(add(2,4),6)

if __name__ == '__main__':
    unittest.main()