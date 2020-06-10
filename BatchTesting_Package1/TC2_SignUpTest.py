import unittest

class SignUpTest(unittest.TestCase):

    def test_signByEmail(self):
        print("This is signup by email test")
        self.assertTrue(True)

    def test_signByFaceBook(self):
        print("This is signup by Facebook")
        self.assertTrue(True)

    def test_signByTwitter(self):
        print("This is signup by Tweeter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()