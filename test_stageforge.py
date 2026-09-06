# test_stageforge.py
"""
Tests for StageForge module.
"""

import unittest
from stageforge import StageForge

class TestStageForge(unittest.TestCase):
    """Test cases for StageForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StageForge()
        self.assertIsInstance(instance, StageForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StageForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
