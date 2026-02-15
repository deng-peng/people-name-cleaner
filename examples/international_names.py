"""
International names example

This example demonstrates handling of various international character sets
including Spanish, Chinese, Korean, Cyrillic, Vietnamese, and Arabic names.

Run this script from the repository root:
    python3 examples/international_names.py
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from FullNameCleaner import FullNameCleaner
from FullNameParser import FullNameParser


def main():
    print("=" * 70)
    print("People Name Cleaner - International Names Example")
    print("=" * 70)
    print()

    # Initialize cleaner and parser
    cleaner = FullNameCleaner()
    parser = FullNameParser(cleaner)

    # Example 1: Spanish names with accents
    print("Example 1: Spanish Names")
    print("-" * 70)
    
    spanish_names = [
        'josé garcía',
        'francisco jiménez garcía',
        'maría lópez',
    ]
    
    for name in spanish_names:
        cleaned = cleaner.getCleanFullName(name)
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → Cleaned: {cleaned:25}")
        print(f"  First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 2: Chinese names
    print("Example 2: Chinese Names (Romanized)")
    print("-" * 70)
    
    chinese_names = [
        '冯仰利',
        '旭 姚',
    ]
    
    for name in chinese_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 3: Korean names
    print("Example 3: Korean Names")
    print("-" * 70)
    
    korean_names = [
        '현명 김',
    ]
    
    for name in korean_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 4: Cyrillic names
    print("Example 4: Cyrillic Names (Ukrainian/Russian)")
    print("-" * 70)
    
    cyrillic_names = [
        'олександра миляник',
    ]
    
    for name in cyrillic_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 5: Vietnamese names
    print("Example 5: Vietnamese Names")
    print("-" * 70)
    
    vietnamese_names = [
        'huệ trần',
    ]
    
    for name in vietnamese_names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:30} → First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 6: Mixed international names with special characters
    print("Example 6: Names with Special Characters")
    print("-" * 70)
    
    special_names = [
        'mohammed abdul aziz syed ☁',
        'thaddeus "matt" biagas',
    ]
    
    for name in special_names:
        cleaned = cleaner.getCleanFullName(name)
        first_last = parser.getFirstAndLastName(name)
        print(f"Original: {name:35}")
        print(f"  Cleaned: {cleaned:30}")
        print(f"  First: {first_last[0]:15} Last: {first_last[1]}")
        print()


if __name__ == '__main__':
    main()
