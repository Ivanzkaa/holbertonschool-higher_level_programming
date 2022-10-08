#!/usr/bin/python3
"""Test base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_file_for_base(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_idParam(self):
        base4 = Base(23)
        base5 = Base(45)
        self.assertEqual(base4.id, 23)
        self.assertEqual(base5.id, 45)

    def test_negative(self):
        base1 = Base(-2)
        base2 = Base(-10)
        self.assertEqual(base1.id, -2)
        self.assertEqual(base2.id, -10)

    def test_string(self):
        base1 = Base("python")
        base2 = Base("language")
        self.assertEqual(base1.id, "python")
        self.assertEqual(base2.id, "language")

    def test_if_none(self):
        base1 = Base()
        base2 = Base(None)
        self.assertNotEqual(base1.id, 1)
        self.assertNotEqual(base2.id, 21)
