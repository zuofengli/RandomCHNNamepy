from RandomName import RandomName
import unittest
import sys


class RandomNameTests(unittest.TestCase):
    def setUp(self):
        if sys.version_info > (3, 0):
            self.assertRegexp = self.assertRegex
        else:
            self.assertRegexp = self.assertRegexpMatches

    def testRandomName(self):
        randomname70 = RandomName()
        for i in range(0, 10):
            print(randomname70.randomname(age=70))
        randomname80 = RandomName()
        for i in range(0, 10):
            print(randomname80.randomname(age=80))


if __name__ == '__main__':
    unittest.main()
