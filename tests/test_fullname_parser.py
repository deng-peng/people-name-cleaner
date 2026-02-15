"""
Unit tests for FullNameParser class

These tests verify that the FullNameParser properly extracts first, middle,
and last names from cleaned full names.
"""

import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from FullNameCleaner import FullNameCleaner
from FullNameParser import FullNameParser


class TestFullNameParser(unittest.TestCase):
    """Test cases for FullNameParser class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = FullNameCleaner()
        self.parser = FullNameParser(self.cleaner)
    
    def test_get_first_name_simple(self):
        """Test extracting first name from simple full name"""
        result = self.parser.getFirstName('john smith')
        self.assertEqual(result, 'john')
    
    def test_get_last_name_simple(self):
        """Test extracting last name from simple full name"""
        result = self.parser.getLastName('john smith')
        self.assertEqual(result, 'smith')
    
    def test_get_first_and_last_name(self):
        """Test extracting both first and last name"""
        result = self.parser.getFirstAndLastName('john smith')
        self.assertEqual(result, ['john', 'smith'])
    
    def test_get_middle_name_three_parts(self):
        """Test extracting middle name from three-part name"""
        result = self.parser.getMiddleName('john michael smith')
        self.assertEqual(result, 'michael')
    
    def test_get_first_middle_last_name(self):
        """Test extracting all three parts"""
        result = self.parser.getFirstMiddleLastName('john michael smith')
        self.assertEqual(result, ['john', 'michael', 'smith'])
    
    def test_single_name(self):
        """Test parsing a single name"""
        result = self.parser.getFirstAndLastName('madonna')
        self.assertEqual(result, ['madonna', ''])
    
    def test_two_names(self):
        """Test parsing a two-part name"""
        result = self.parser.getFirstMiddleLastName('john smith')
        self.assertEqual(result, ['john', '', 'smith'])
    
    def test_four_part_name(self):
        """Test parsing a four-part name (two middle names)"""
        result = self.parser.getFirstMiddleLastName('mohammed abdul aziz syed')
        self.assertEqual(result[0], 'mohammed')
        self.assertEqual(result[2], 'syed')
        # Middle name should contain the middle parts
        self.assertIn('abdul', result[1])
        self.assertIn('aziz', result[1])
    
    def test_spanish_name_with_accents(self):
        """Test parsing Spanish name with accents"""
        result = self.parser.getFirstAndLastName('francisco jiménez garcía')
        self.assertEqual(result, ['francisco', 'garcia'])
    
    def test_name_with_title(self):
        """Test parsing name with title"""
        result = self.parser.getFirstAndLastName('Dr. John Smith')
        self.assertEqual(result, ['john', 'smith'])
    
    def test_name_with_suffix(self):
        """Test parsing name with suffix"""
        result = self.parser.getFirstAndLastName('Felix Watson Jr.')
        self.assertEqual(result, ['felix', 'watson'])
    
    def test_name_with_comma(self):
        """Test parsing name with comma and title"""
        result = self.parser.getFirstAndLastName('rob liu, ceo')
        self.assertEqual(result, ['rob', 'liu'])
    
    def test_multipart_surname_van_der(self):
        """Test parsing name with Van Der surname"""
        result = self.parser.getFirstAndLastName('Katie Van Der Lala')
        self.assertEqual(result[0], 'katie')
        # Last name should include the multipart surname
        self.assertIn('lala', result[1])
    
    def test_multipart_surname_de(self):
        """Test parsing name with De surname"""
        result = self.parser.getFirstAndLastName('Katie De Lala')
        self.assertEqual(result[0], 'katie')
        self.assertIn('lala', result[1])
    
    def test_linkedin_style_suffix(self):
        """Test parsing LinkedIn-style name"""
        result = self.parser.getFirstAndLastName('john smith • 2nd')
        self.assertEqual(result, ['john', 'smith'])
    
    def test_name_with_quotes(self):
        """Test parsing name with quotes"""
        result = self.parser.getFirstAndLastName('thaddeus "matt" biagas')
        self.assertEqual(result, ['thaddeus', 'biagas'])
    
    def test_empty_string(self):
        """Test parsing empty string"""
        result = self.parser.getFirstAndLastName('')
        self.assertEqual(result, ['', ''])
    
    def test_chinese_name(self):
        """Test parsing Chinese name (romanized)"""
        result = self.parser.getFirstAndLastName('冯仰利')
        # Should have romanized first and last names
        self.assertNotEqual(result[0], '')
        self.assertNotEqual(result[1], '')
    
    def test_korean_name(self):
        """Test parsing Korean name"""
        result = self.parser.getFirstAndLastName('현명 김')
        # Should have romanized first and last names
        self.assertNotEqual(result[0], '')
        self.assertNotEqual(result[1], '')
    
    def test_cyrillic_name(self):
        """Test parsing Cyrillic name"""
        result = self.parser.getFirstAndLastName('олександра миляник')
        self.assertEqual(result[0], 'oleksandra')
        # The romanization is 'milianik'
        self.assertIn('mili', result[1])
    
    def test_vietnamese_name(self):
        """Test parsing Vietnamese name"""
        result = self.parser.getFirstAndLastName('huệ trần')
        # Should have romanized first and last names
        self.assertNotEqual(result[0], '')
        self.assertNotEqual(result[1], '')


class TestFullNameParserFiltering(unittest.TestCase):
    """Test English filtering options in FullNameParser"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = FullNameCleaner()
        self.parser = FullNameParser(self.cleaner)
    
    def test_filter_english_enabled(self):
        """Test parsing with English filtering enabled"""
        self.parser.setFilterEnglist(True)
        result = self.parser.getFirstAndLastName('josé garcía')
        # Should convert to English characters
        self.assertEqual(result[0], 'jose')
        self.assertEqual(result[1], 'garcia')
    
    def test_filter_english_disabled(self):
        """Test parsing with English filtering disabled"""
        self.parser.setFilterEnglist(False)
        result = self.parser.getFirstAndLastName('josé garcía')
        # Should still convert accents but not filter
        self.assertEqual(result[0], 'jose')
        self.assertEqual(result[1], 'garcia')


class TestFullNameParserEdgeCases(unittest.TestCase):
    """Test edge cases for FullNameParser"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cleaner = FullNameCleaner()
        self.parser = FullNameParser(self.cleaner)
    
    def test_name_with_numbers(self):
        """Test parsing name with numbers"""
        result = self.parser.getFirstAndLastName('Joel 123 R. Quinn, PMP')
        self.assertEqual(result[0], 'joel')
        self.assertEqual(result[1], 'quinn')
    
    def test_name_with_only_title(self):
        """Test parsing name that's only a title"""
        result = self.parser.getFirstAndLastName('Dr.')
        self.assertEqual(result, ['', ''])
    
    def test_very_long_middle_name(self):
        """Test parsing name with many middle names"""
        result = self.parser.getFirstMiddleLastName('john a b c d smith')
        self.assertEqual(result[0], 'john')
        self.assertEqual(result[2], 'smith')
        # Middle should contain all middle parts
        self.assertIn('a', result[1])
        self.assertIn('d', result[1])


if __name__ == '__main__':
    unittest.main()
