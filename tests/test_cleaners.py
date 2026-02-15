"""
Unit tests for individual cleaner modules

These tests verify that individual cleaning components work correctly.
"""

import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from RemoveSpecialCharacters import RemoveSpecialCharacters
from RemoveAfterComma import RemoveAfterComma
from RemoveIgnoreHeadLine import RemoveIgnoreHeadLine
from RemovePunctuation import RemovePunctuation
from RemoveExtraEnds import RemoveExtraEnds
from RemoveExtraSpace import RemoveExtraSpace
from RemoveUnEnglish import RemoveUnEnglish
from ConvertSpanishToEnglish import ConvertSpanishToEnglish


class TestRemoveSpecialCharacters(unittest.TestCase):
    """Test RemoveSpecialCharacters module"""
    
    def setUp(self):
        self.cleaner = RemoveSpecialCharacters()
    
    def test_remove_periods(self):
        result = self.cleaner.getCleanFullName('Dr. John Smith Jr.')
        self.assertNotIn('.', result)
        self.assertEqual(result, 'Dr John Smith Jr')


class TestRemoveAfterComma(unittest.TestCase):
    """Test RemoveAfterComma module"""
    
    def setUp(self):
        self.cleaner = RemoveAfterComma()
    
    def test_remove_after_comma(self):
        result = self.cleaner.getCleanFullName('John Smith, CEO')
        self.assertEqual(result, 'John Smith')
    
    def test_no_comma(self):
        result = self.cleaner.getCleanFullName('John Smith')
        self.assertEqual(result, 'John Smith')
    
    def test_multiple_commas(self):
        result = self.cleaner.getCleanFullName('John Smith, CEO, PhD')
        self.assertEqual(result, 'John Smith')


class TestRemoveIgnoreHeadLine(unittest.TestCase):
    """Test RemoveIgnoreHeadLine module"""
    
    def setUp(self):
        self.cleaner = RemoveIgnoreHeadLine()
    
    def test_remove_title_dr(self):
        result = self.cleaner.getCleanFullName('dr john smith')
        self.assertNotIn('dr', result.split())
    
    def test_remove_suffix_jr(self):
        result = self.cleaner.getCleanFullName('john smith jr')
        self.assertNotIn('jr', result.split())
    
    def test_remove_phd(self):
        result = self.cleaner.getCleanFullName('jane doe phd')
        self.assertNotIn('phd', result.split())
    
    def test_preserve_normal_words(self):
        result = self.cleaner.getCleanFullName('john smith')
        self.assertIn('john', result)
        self.assertIn('smith', result)


class TestRemovePunctuation(unittest.TestCase):
    """Test RemovePunctuation module"""
    
    def setUp(self):
        self.cleaner = RemovePunctuation()
    
    def test_remove_parentheses(self):
        result = self.cleaner.getCleanFullName('John (Jack) Smith')
        self.assertNotIn('(', result)
        self.assertNotIn(')', result)
        self.assertNotIn('Jack', result)
    
    def test_remove_brackets(self):
        result = self.cleaner.getCleanFullName('Mary [Jane] Doe')
        self.assertNotIn('[', result)
        self.assertNotIn(']', result)
        self.assertNotIn('Jane', result)
    
    def test_remove_braces(self):
        result = self.cleaner.getCleanFullName('Bob {Robert} Smith')
        self.assertNotIn('{', result)
        self.assertNotIn('}', result)
        self.assertNotIn('Robert', result)


class TestRemoveExtraEnds(unittest.TestCase):
    """Test RemoveExtraEnds module"""
    
    def setUp(self):
        self.cleaner = RemoveExtraEnds()
    
    def test_remove_linkedin_1st(self):
        result = self.cleaner.getCleanFullName('John Smith • 1st')
        self.assertNotIn('•', result)
        self.assertEqual(result, 'John Smith')
    
    def test_remove_linkedin_2nd(self):
        result = self.cleaner.getCleanFullName('Jane Doe • 2nd')
        self.assertNotIn('•', result)
        self.assertEqual(result, 'Jane Doe')
    
    def test_remove_linkedin_3rd(self):
        result = self.cleaner.getCleanFullName('Bob Johnson • 3rd+')
        self.assertNotIn('•', result)
        self.assertEqual(result, 'Bob Johnson')
    
    def test_no_linkedin_suffix(self):
        result = self.cleaner.getCleanFullName('John Smith')
        self.assertEqual(result, 'John Smith')


class TestRemoveExtraSpace(unittest.TestCase):
    """Test RemoveExtraSpace module"""
    
    def setUp(self):
        self.cleaner = RemoveExtraSpace()
    
    def test_trim_leading_space(self):
        result = self.cleaner.getCleanFullName('  John Smith')
        self.assertEqual(result, 'John Smith')
    
    def test_trim_trailing_space(self):
        result = self.cleaner.getCleanFullName('John Smith  ')
        self.assertEqual(result, 'John Smith')
    
    def test_trim_both_spaces(self):
        result = self.cleaner.getCleanFullName('  John Smith  ')
        self.assertEqual(result, 'John Smith')


class TestRemoveUnEnglish(unittest.TestCase):
    """Test RemoveUnEnglish module"""
    
    def setUp(self):
        self.cleaner = RemoveUnEnglish()
    
    def test_remove_emoji(self):
        result = self.cleaner.getCleanFullName('John Smith ☁')
        self.assertNotIn('☁', result)
    
    def test_keep_letters_and_numbers(self):
        result = self.cleaner.getCleanFullName('John123 Smith456')
        self.assertIn('John123', result)
        self.assertIn('Smith456', result)
    
    def test_keep_periods_and_hyphens(self):
        result = self.cleaner.getCleanFullName('Jean-Paul Smith')
        self.assertIn('-', result)


class TestConvertSpanishToEnglish(unittest.TestCase):
    """Test ConvertSpanishToEnglish module"""
    
    def setUp(self):
        self.cleaner = ConvertSpanishToEnglish()
    
    def test_convert_spanish_accents(self):
        result = self.cleaner.getCleanFullName('josé garcía')
        self.assertEqual(result, 'jose garcia')
    
    def test_convert_spanish_n_tilde(self):
        result = self.cleaner.getCleanFullName('señor')
        self.assertEqual(result, 'senor')
    
    def test_convert_various_accents(self):
        result = self.cleaner.getCleanFullName('àáâãäåèéêëìíîï')
        # Should convert all accented characters
        self.assertNotIn('á', result)
        self.assertNotIn('é', result)


if __name__ == '__main__':
    unittest.main()
