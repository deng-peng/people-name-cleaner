"""
Test runner for all tests

Run all tests with:
    python3 tests/run_all_tests.py

Or run individual test files:
    python3 -m unittest tests.test_fullname_cleaner -v
"""

import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import test modules
from test_fullname_cleaner import TestFullNameCleaner, TestFullNameCleanerEdgeCases
from test_fullname_parser import TestFullNameParser, TestFullNameParserFiltering, TestFullNameParserEdgeCases
from test_cleaners import (
    TestRemoveSpecialCharacters,
    TestRemoveAfterComma,
    TestRemoveIgnoreHeadLine,
    TestRemovePunctuation,
    TestRemoveExtraEnds,
    TestRemoveExtraSpace,
    TestRemoveUnEnglish,
    TestConvertSpanishToEnglish
)


def run_all_tests():
    """Run all tests and return the results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestFullNameCleaner))
    suite.addTests(loader.loadTestsFromTestCase(TestFullNameCleanerEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestFullNameParser))
    suite.addTests(loader.loadTestsFromTestCase(TestFullNameParserFiltering))
    suite.addTests(loader.loadTestsFromTestCase(TestFullNameParserEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveSpecialCharacters))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveAfterComma))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveIgnoreHeadLine))
    suite.addTests(loader.loadTestsFromTestCase(TestRemovePunctuation))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveExtraEnds))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveExtraSpace))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveUnEnglish))
    suite.addTests(loader.loadTestsFromTestCase(TestConvertSpanishToEnglish))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    result = run_all_tests()
    
    # Exit with non-zero code if there were failures
    sys.exit(0 if result.wasSuccessful() else 1)
