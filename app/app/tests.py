"""
    Simple Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_function(self):
        """Test adding numbers together."""
        x = 5
        y = 6
        res = calc.add(x, y)
        self.assertEqual(res, 11)
        
    def test_sub_function(self):
        """Test subtracting number from number."""
        x = 10
        y = 15
        res = calc.sub(x, y)
        self.assertEqual(res, 5)