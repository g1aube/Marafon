import unittest

def func(x, y):
    return x + y

class TestCase(unittest.TestCase):
    def check_test(self):
        self.assertEqual(func(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
