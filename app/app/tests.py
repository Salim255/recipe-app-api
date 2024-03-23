"""
Sample test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(6, 3)
        self.assertEqual(res, 3)
