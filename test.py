import unittest
from command import is_equal
# from five import is_equal


class Equal(unittest.TestCase):
    def test(self):
        self.assertTrue(is_equal(4, 4))


if __name__ == '__main__':
    print('nani')
    unittest.main()
