#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_integers(self):
        self.assertEqual(max_integer([500, 30, -25, 44]), 500)
        self.assertEqual(max_integer([-20, 0, -100, -60]), 0)

    def test_string(self):
        self.assertEqual(max_integer(["Make America", "Great again"]),
                         "Make America")

    def test_float(self):
        self.assertEqual(max_integer([0.1, -3.4, -67]), 0.1)

    def test_doc(self):
        self.assertIsNotNone(max_integer.__doc__)


if __name__ == '__main__':
    unittest.main()