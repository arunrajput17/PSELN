#### Relational comparison
# assertGreater verifies whether first values if greater than second value or not.
# assertGreaterEqual verifies whether first parameter is greater or equal to the second parameter.
# assertLess verifies whether first parameter is lesser than second parameter or not.
# assertLessEqual verifies whether first parameter is lesser or equal to the second parameter.

import unittest

class Test(unittest.TestCase):
    def testName1(self):
        self.assertGreater(100,10)

    def testName2(self):
        self.assertGreaterEqual(10,10)

    def testName3(self):
        self.assertLess(9,10)

    def testName4(self):
        self.assertLessEqual(10,10)


if __name__ == "__main__":
    unittest.main()
