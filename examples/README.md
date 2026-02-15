# Examples

This directory contains practical examples of using the people-name-cleaner library.

## Available Examples

### 1. basic_usage.py
Demonstrates basic functionality including:
- Cleaning names with titles and suffixes
- Extracting first and last names
- Parsing names into components (first, middle, last)

Run with:
```bash
python3 examples/basic_usage.py
```

### 2. international_names.py
Shows handling of international character sets:
- Spanish names with accents
- Chinese names (romanized)
- Korean names
- Cyrillic names (Ukrainian/Russian)
- Vietnamese names
- Names with special characters and emojis

Run with:
```bash
python3 examples/international_names.py
```

### 3. advanced_usage.py
Demonstrates advanced features:
- Controlling English character filtering
- LinkedIn-style names with suffixes
- Professional titles and designations
- Multi-part surnames (European style)
- Names with punctuation and brackets
- Edge cases

Run with:
```bash
python3 examples/advanced_usage.py
```

## Running All Examples

To run all examples at once:
```bash
python3 examples/basic_usage.py
python3 examples/international_names.py
python3 examples/advanced_usage.py
```

Or create a simple script to run them all sequentially.
