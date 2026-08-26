# test_oathjolt.py
"""
Tests for OathJolt module.
"""

import unittest
from oathjolt import OathJolt

class TestOathJolt(unittest.TestCase):
    """Test cases for OathJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OathJolt()
        self.assertIsInstance(instance, OathJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OathJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
