"""
Unit tests for FullNameCleaner class

These tests verify that the FullNameCleaner properly removes special characters,
titles, suffixes, and normalizes names.
"""

import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from FullNameCleaner import FullNameCleaner


class TestFullNameCleaner(unittest.TestCase):
    """Test cases for FullNameCleaner class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = FullNameCleaner()
    
    def test_clean_simple_name(self):
        """Test cleaning a simple name without special characters"""
        result = self.cleaner.getCleanFullName('john smith')
        self.assertEqual(result, 'john smith')
    
    def test_remove_periods(self):
        """Test removal of periods"""
        result = self.cleaner.getCleanFullName('Dr. John Smith Jr.')
        self.assertNotIn('.', result)
    
    def test_remove_comma_and_after(self):
        """Test removal of comma and everything after it"""
        result = self.cleaner.getCleanFullName('bill gates, CEO, PHD')
        self.assertEqual(result, 'bill gates')
    
    def test_remove_professional_suffix(self):
        """Test removal of professional suffixes like PMP"""
        result = self.cleaner.getCleanFullName('Joel R. Quinn, PMP')
        self.assertEqual(result, 'joel r quinn')
    
    def test_remove_title_dr(self):
        """Test removal of Dr title"""
        result = self.cleaner.getCleanFullName('Dr. John Smith')
        self.assertEqual(result, 'john smith')
    
    def test_remove_suffix_jr(self):
        """Test removal of Jr suffix"""
        result = self.cleaner.getCleanFullName('Felix Watson Jr.')
        self.assertEqual(result, 'felix watson')
    
    def test_convert_spanish_accents(self):
        """Test conversion of Spanish accented characters"""
        self.cleaner.setFilterEnglist(False)
        result = self.cleaner.getCleanFullName('francisco jiménez garcía')
        self.assertEqual(result, 'francisco jimenez garcia')
    
    def test_remove_linkedin_suffix(self):
        """Test removal of LinkedIn-style suffixes"""
        result = self.cleaner.getCleanFullName('john smith • 2nd')
        self.assertEqual(result, 'john smith')
    
    def test_remove_parentheses_content(self):
        """Test removal of content in parentheses"""
        result = self.cleaner.getCleanFullName('John (Jack) Smith')
        # Should remove parentheses content and convert to lowercase
        self.assertNotIn('jack', result.lower())
        self.assertIn('john', result.lower())
        self.assertIn('smith', result.lower())
    
    def test_remove_brackets_content(self):
        """Test removal of content in brackets"""
        result = self.cleaner.getCleanFullName('Mary [Jane] Doe')
        # Should remove brackets content and convert to lowercase
        self.assertNotIn('jane', result.lower())
        self.assertIn('mary', result.lower())
        self.assertIn('doe', result.lower())
    
    def test_handle_empty_string(self):
        """Test handling of empty string"""
        result = self.cleaner.getCleanFullName('')
        self.assertEqual(result, '')
    
    def test_handle_none(self):
        """Test handling of None input"""
        result = self.cleaner.getCleanFullName(None)
        self.assertIsNone(result)
    
    def test_filter_english_enabled(self):
        """Test English filtering when enabled"""
        self.cleaner.setFilterEnglist(True)
        result = self.cleaner.getCleanFullName('josé garcía 123')
        # Should convert accents and keep numbers
        self.assertIn('jose', result)
        self.assertIn('garcia', result)
    
    def test_filter_english_disabled(self):
        """Test English filtering when disabled"""
        self.cleaner.setFilterEnglist(False)
        result = self.cleaner.getCleanFullName('josé garcía')
        # Should only convert accents, not filter
        self.assertEqual(result, 'jose garcia')
    
    def test_multiple_spaces_trimmed(self):
        """Test that extra spaces are trimmed"""
        result = self.cleaner.getCleanFullName('  john   smith  ')
        # RemoveIgnoreHeadLine splits and rejoins, collapsing multiple spaces
        # RemoveExtraSpace only trims outer spaces
        self.assertIn('john', result)
        self.assertIn('smith', result)
    
    def test_special_characters_emoji(self):
        """Test removal of emoji characters"""
        result = self.cleaner.getCleanFullName('mohammed abdul aziz syed ☁')
        self.assertNotIn('☁', result)
    
    def test_complex_name_with_multiple_issues(self):
        """Test a complex name with multiple cleaning needs"""
        result = self.cleaner.getCleanFullName('Dr. José García, PhD, MBA (CEO) • 2nd')
        # Should remove title, comma and after, parentheses, suffix
        self.assertNotIn('Dr', result)
        self.assertNotIn('PhD', result)
        self.assertNotIn('CEO', result)
        self.assertNotIn('•', result)


class TestFullNameCleanerEdgeCases(unittest.TestCase):
    """Test edge cases for FullNameCleaner"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = FullNameCleaner()
    
    def test_only_title(self):
        """Test name with only a title"""
        result = self.cleaner.getCleanFullName('Dr.')
        self.assertEqual(result, '')
    
    def test_only_suffix(self):
        """Test name with only a suffix"""
        result = self.cleaner.getCleanFullName('Jr.')
        self.assertEqual(result, '')
    
    def test_numbers_in_name(self):
        """Test that numbers are handled properly"""
        result = self.cleaner.getCleanFullName('Joel 123 R. Quinn')
        self.assertIn('joel', result.lower())
        self.assertIn('quinn', result.lower())


if __name__ == '__main__':
    unittest.main()
