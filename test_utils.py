import unittest

import utils


class TestUtils(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(utils.say_hello("Juan"), "Hello, Juan")
        self.assertEqual(utils.say_hello("Pepe"), "Hello, Pepe")
        self.assertNotEqual(utils.say_hello("Carlos"), "Hi, Carlos")
        self.assertNotEqual(utils.say_hello("Jose"), "Hi, Jose")


if __name__ == '__main__':
    unittest.main()
