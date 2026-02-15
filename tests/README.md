# Tests

This directory contains comprehensive unit tests for the people-name-cleaner library.

## Test Structure

- **test_fullname_cleaner.py**: Tests for the FullNameCleaner class (20 tests)
- **test_fullname_parser.py**: Tests for the FullNameParser class (29 tests)
- **test_cleaners.py**: Tests for individual cleaner modules (21 tests)
- **run_all_tests.py**: Test runner that executes all tests

## Running Tests

### Run All Tests
```bash
python3 tests/run_all_tests.py
```

### Run Specific Test Files
```bash
# Test FullNameCleaner
python3 -m unittest tests.test_fullname_cleaner -v

# Test FullNameParser
python3 -m unittest tests.test_fullname_parser -v

# Test individual cleaner modules
python3 -m unittest tests.test_cleaners -v
```

### Run Specific Test Cases
```bash
# Run a specific test class
python3 -m unittest tests.test_fullname_cleaner.TestFullNameCleaner -v

# Run a specific test method
python3 -m unittest tests.test_fullname_cleaner.TestFullNameCleaner.test_clean_simple_name -v
```

## Test Coverage

The test suite includes **70 tests** covering:

### FullNameCleaner Tests (20 tests)
- Simple name cleaning
- Period removal
- Comma and suffix removal
- Title removal (Dr., Prof., etc.)
- Suffix removal (Jr., Sr., PhD, etc.)
- Spanish accent conversion
- LinkedIn suffix removal
- Parentheses/brackets content removal
- Empty string and None handling
- English filtering options
- Multi-space trimming
- Emoji and special character removal
- Complex names with multiple issues
- Edge cases (only title, only suffix, numbers in names)

### FullNameParser Tests (29 tests)
- First name extraction
- Last name extraction
- Middle name extraction
- First and last name extraction
- Full name parsing (first, middle, last)
- Single name handling
- Two-part names
- Multi-part names (4+ parts)
- Spanish names with accents
- Names with titles and suffixes
- Names with commas
- Multi-part surnames (Van Der, De La, etc.)
- LinkedIn-style names
- Names with quotes
- Empty string handling
- International names (Chinese, Korean, Cyrillic, Vietnamese)
- English filtering options
- Edge cases (numbers in names, only titles, very long middle names)

### Individual Cleaner Module Tests (21 tests)
- RemoveSpecialCharacters: Period removal
- RemoveAfterComma: Comma handling, multiple commas
- RemoveIgnoreHeadLine: Title/suffix removal, word preservation
- RemovePunctuation: Parentheses, brackets, braces removal
- RemoveExtraEnds: LinkedIn suffix removal (• 1st, • 2nd, • 3rd+)
- RemoveExtraSpace: Leading/trailing space trimming
- RemoveUnEnglish: Emoji removal, letter/number preservation
- ConvertSpanishToEnglish: Accent conversion, ñ conversion

## Test Results

All 70 tests pass successfully, validating:
- Name cleaning and normalization
- First, middle, and last name extraction
- International character handling
- Edge cases and error conditions
- Individual cleaner module functionality
