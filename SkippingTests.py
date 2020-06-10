# ********** Tutorial 32: Skipping Tests
#   Skip test (Skip test without reason)
#   Skip test with reason
#   Skip test with based on condition.



import unittest
class unitTestFramework_demo1(unittest.TestCase):

    @unittest.SkipTest # decorator --> #   Skip test (Skip test without reason)
    def test_search(self):
        print(" 1 This is search page")

    @unittest.skip("I am skipping this below test method because of it has to be implemented") # --> Skip test with reason
    def test_advance_search(self):
        print("2 This is advance search")

    @unittest.skipIf(1==1, "Numbers are equals") # --> Skip test with based on condition
    def test_prepaid_recharge(self):
        print("3 This is prepaid recharge")

    def test_postpaid_recharge(self):
        print("4 This is postpaid recharge")


if __name__ == '__main__':
    unittest.main()