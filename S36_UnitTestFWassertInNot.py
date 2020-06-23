#### assertIn:
# assertIn method verifies whether the first element is present in the send element, if the first 
# element is present in second element then test is passed otherwise test is failed.
# 
#### assertNotIn:
# assertNotIn method verifies the first element is not present in the second element or not, if 
# first element is present then the test will be failed otherwise test is passed
# 
# -- These two elements will be helpful when you want to verify presence of a value in a list, 
# tuple, set, and dictionary.

import unittest


class Test(unittest.TestCase):
    def testName(self):
        list=('python','selenium','java')

        # assertIn
        self.assertIn('python',list)
    
    def testName1(self):
        list=('python','selenium','java')

        # assertNotIn
        self.assertNotIn('ruby',list)



if __name__ == "__main__":
    unittest.main()
