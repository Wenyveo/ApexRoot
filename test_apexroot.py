# test_apexroot.py
"""
Tests for ApexRoot module.
"""

import unittest
from apexroot import ApexRoot

class TestApexRoot(unittest.TestCase):
    """Test cases for ApexRoot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexRoot()
        self.assertIsInstance(instance, ApexRoot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexRoot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
