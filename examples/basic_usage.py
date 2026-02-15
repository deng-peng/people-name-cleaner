"""
Basic example of using people-name-cleaner library

This example demonstrates the basic usage of FullNameCleaner and FullNameParser
to clean and parse names.

Run this script from the repository root:
    python3 examples/basic_usage.py
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from FullNameCleaner import FullNameCleaner
from FullNameParser import FullNameParser


def main():
    print("=" * 60)
    print("People Name Cleaner - Basic Example")
    print("=" * 60)
    print()

    # Initialize cleaner and parser
    cleaner = FullNameCleaner()
    parser = FullNameParser(cleaner)

    # Example 1: Clean names with titles and suffixes
    print("Example 1: Cleaning Names with Titles and Suffixes")
    print("-" * 60)
    
    names = [
        'Dr. John Smith',
        'Jane Doe, PhD',
        'Bob Johnson Jr.',
        'Prof. Alice Williams, MD',
    ]
    
    for name in names:
        cleaned = cleaner.getCleanFullName(name)
        print(f"Original: {name:30} → Cleaned: {cleaned}")
    print()

    # Example 2: Extract first and last names
    print("Example 2: Extracting First and Last Names")
    print("-" * 60)
    
    names = [
        'francisco jiménez garcía',
        'John Michael Smith',
        'Mary Ann Johnson',
    ]
    
    for name in names:
        first_last = parser.getFirstAndLastName(name)
        print(f"Name: {name:30} → First: {first_last[0]:15} Last: {first_last[1]}")
    print()

    # Example 3: Parse full name into components
    print("Example 3: Parsing Names into Components")
    print("-" * 60)
    
    names = [
        'Katie Van Der Lala',
        'Mohammed Abdul Aziz Syed',
        'daniela pilar caquimbo yustres',
    ]
    
    for name in names:
        parts = parser.getFirstMiddleLastName(name)
        print(f"Name: {name}")
        print(f"  First:  {parts[0]}")
        print(f"  Middle: {parts[1]}")
        print(f"  Last:   {parts[2]}")
        print()


if __name__ == '__main__':
    main()
