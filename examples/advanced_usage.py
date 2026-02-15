"""
Advanced usage example

This example demonstrates advanced features including filtering options,
handling complex name formats, and edge cases.

Run this script from the repository root:
    python3 examples/advanced_usage.py
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from FullNameCleaner import FullNameCleaner
from FullNameParser import FullNameParser


def main():
    print("=" * 70)
    print("People Name Cleaner - Advanced Usage Example")
    print("=" * 70)
    print()

    # Example 1: English filtering control
    print("Example 1: Controlling English Character Filtering")
    print("-" * 70)
    
    cleaner = FullNameCleaner()
    name = 'josé garcía 123'
    
    # With English filtering (default)
    cleaner.setFilterEnglist(True)
    cleaned_filtered = cleaner.getCleanFullName(name)
    print(f"Original: {name}")
    print(f"With English filtering (default): {cleaned_filtered}")
    
    # Without English filtering
    cleaner.setFilterEnglist(False)
    cleaned_unfiltered = cleaner.getCleanFullName(name)
    print(f"Without English filtering:        {cleaned_unfiltered}")
    print()

    # Example 2: LinkedIn-style names
    print("Example 2: LinkedIn-Style Names with Suffixes")
    print("-" * 70)
    
    parser = FullNameParser(FullNameCleaner())
    
    linkedin_names = [
        'jisdsd sdfdfd cto (1231232131) • 2nd',
        "'inoke • 2nd",
        'john smith • 1st',
    ]
    
    for name in linkedin_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:45} → First: {first_last[0]:12} Last: {first_last[1]}")
    print()

    # Example 3: Names with professional titles and designations
    print("Example 3: Professional Titles and Designations")
    print("-" * 70)
    
    professional_names = [
        'rob liu, ceo',
        'bill gates, CEO, PHD',
        'Joel R. Quinn, PMP',
        'Dr. Sarah Johnson, MD, PhD',
    ]
    
    for name in professional_names:
        cleaned = cleaner.getCleanFullName(name)
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:35}")
        print(f"  Cleaned: {cleaned:30}")
        print(f"  First: {first_last[0]:12} Last: {first_last[1]}")
        print()

    # Example 4: Multi-part surnames (European style)
    print("Example 4: Multi-Part Surnames")
    print("-" * 70)
    
    multipart_names = [
        'Katie De Lala',
        'Katie Van Der Lala',
        'Katie Della Lala',
        'Katie Du Lala',
        'mohammed al attar',
    ]
    
    for name in multipart_names:
        parts = parser.getFirstMiddleLastName(name)
        print(f"Name: {name:30}")
        print(f"  First: {parts[0]:10} Middle: {parts[1]:15} Last: {parts[2]}")
    print()

    # Example 5: Names with various punctuation
    print("Example 5: Names with Punctuation and Brackets")
    print("-" * 70)
    
    punctuation_names = [
        'thaddeus "matt" biagas',
        'John (Jack) Smith',
        'Mary [Jane] Doe',
    ]
    
    for name in punctuation_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → First: {first_last[0]:12} Last: {first_last[1]}")
    print()

    # Example 6: Edge cases
    print("Example 6: Edge Cases")
    print("-" * 70)
    
    edge_cases = [
        ('Single name', 'Madonna'),
        ('Empty string', ''),
        ('Only title', 'Dr.'),
        ('Numbers in name', 'Joel 123 R. Quinn, PMP'),
    ]
    
    for description, name in edge_cases:
        try:
            first_last = parser.getFirstAndLastName(name) if name else ['', '']
            print(f"{description:25} → First: '{first_last[0]}'  Last: '{first_last[1]}'")
        except Exception as e:
            print(f"{description:25} → Error: {e}")
    print()


if __name__ == '__main__':
    main()
