# People Name Cleaner

A Python library for cleaning and parsing people's names from various formats. This library handles messy name data by removing titles, suffixes, special characters, and extracting first, middle, and last names intelligently.

## Features

- **Name Cleaning**: Remove special characters, punctuation, titles (Dr., Jr., PhD, etc.), and professional suffixes
- **Name Parsing**: Extract first name, middle name, and last name from full names
- **International Support**: Convert non-English characters to English equivalents (e.g., Spanish accents)
- **Flexible Filtering**: Optional filtering for English-only characters
- **Smart Processing**: Handles various name formats including:
  - Names with titles and suffixes (Dr. John Smith Jr., PhD)
  - Names with commas (Smith, John)
  - Names with special characters and emojis
  - International names with diacritics (José García)
  - Multi-part surnames (Van Der Berg, De La Cruz)
  - LinkedIn-style suffixes (• 1st, • 2nd, • 3rd+)

## Installation

### Using pip

```bash
pip install -r requirements.txt
```

### From source

```bash
git clone https://github.com/deng-peng/people-name-cleaner.git
cd people-name-cleaner
pip install -r requirements.txt
```

## Requirements

- Python 3.6+
- unidecode>=1.3.0

## Usage

### Basic Usage - Cleaning Names

The `FullNameCleaner` class cleans and normalizes full names by removing unwanted elements:

```python
from src.FullNameCleaner import FullNameCleaner

cleaner = FullNameCleaner()

# Clean a name with Spanish accents
name = cleaner.getCleanFullName('francisco jiménez garcía')
print(name)  # Output: 'francisco jimenez garcia'

# Clean a name with title and suffix
name = cleaner.getCleanFullName('bill gates, CEO, PHD')
print(name)  # Output: 'bill gates'

# Clean a name with professional designation
name = cleaner.getCleanFullName('Joel R. Quinn, PMP')
print(name)  # Output: 'joel r quinn'
```

### Parsing Names - Extracting First and Last Names

The `FullNameParser` class extracts specific parts of a name:

```python
from src.FullNameParser import FullNameParser
from src.FullNameCleaner import FullNameCleaner

parser = FullNameParser(FullNameCleaner())

# Get first and last name
name = 'francisco jiménez garcía'
first_and_last = parser.getFirstAndLastName(name)
print(first_and_last)  # Output: ['francisco', 'garcia']

# Get individual name parts
first = parser.getFirstName(name)
print(first)  # Output: 'francisco'

last = parser.getLastName(name)
print(last)  # Output: 'garcia'

# Get first, middle, and last name
middle_name = parser.getMiddleName(name)
print(middle_name)  # Output: 'jimenez'

all_parts = parser.getFirstMiddleLastName(name)
print(all_parts)  # Output: ['francisco', 'jimenez', 'garcia']
```

### Advanced Usage - International Names

The library handles various international character sets:

```python
from src.FullNameParser import FullNameParser
from src.FullNameCleaner import FullNameCleaner

parser = FullNameParser(FullNameCleaner())

# Chinese name (converts to romanized version)
name = parser.getFirstAndLastName('冯仰利')
print(name)  # Output: ['feng', 'li']

# Korean name
name = parser.getFirstAndLastName('현명 김')
print(name)  # Output: ['hyeonmyeong', 'gim']

# Cyrillic name
name = parser.getFirstAndLastName('олександра миляник')
print(name)  # Output: ['oleksandra', 'miljanik']

# Vietnamese name
name = parser.getFirstAndLastName('huệ trần')
print(name)  # Output: ['hue', 'tran']
```

### Filtering English Characters

You can control whether to filter non-English characters:

```python
from src.FullNameCleaner import FullNameCleaner

cleaner = FullNameCleaner()

# Keep non-English characters
cleaner.setFilterEnglist(False)
name = cleaner.getCleanFullName('josé garcía')
print(name)  # Output: 'jose garcia'

# Filter to English only (default behavior)
cleaner.setFilterEnglist(True)
name = cleaner.getCleanFullName('josé garcía 123')
print(name)  # Output: 'jose garcia'
```

### Handling Complex Names

The library handles various edge cases:

```python
from src.FullNameParser import FullNameParser
from src.FullNameCleaner import FullNameCleaner

parser = FullNameParser(FullNameCleaner())

# Names with LinkedIn suffixes
name = parser.getFirstAndLastName('jisdsd sdfdfd cto (1231232131) • 2nd')
print(name)  # Output: ['jisdsd', 'sdfdfd']

# Names with quotes
name = parser.getFirstAndLastName('thaddeus "matt" biagas')
print(name)  # Output: ['thaddeus', 'biagas']

# Names with titles
name = parser.getFirstAndLastName('Dr. Ofla Herzog')
print(name)  # Output: ['ofla', 'herzog']

# Names with suffixes
name = parser.getFirstAndLastName('Felix Watson Jr.')
print(name)  # Output: ['felix', 'watson']

# Multi-part surnames
name = parser.getFirstAndLastName('Katie Van Der Lala')
print(name)  # Output: ['katie', 'van der lala']
```

## API Reference

### FullNameCleaner

Main class for cleaning full names.

#### Methods

- `__init__()`: Initialize the cleaner with all cleaning modules
- `setFilterEnglist(isFilterEnglish: bool)`: Set whether to filter non-English characters (default: True)
- `getCleanFullName(content: str) -> str`: Clean and normalize a full name

### FullNameParser

Main class for parsing names into components.

#### Methods

- `__init__(fullNameCleaner: FullNameCleaner)`: Initialize with a FullNameCleaner instance
- `setFilterEnglist(isFilterEnglish: bool)`: Set whether to filter non-English characters
- `getFirstName(content: str) -> str`: Extract first name
- `getMiddleName(content: str) -> str`: Extract middle name (empty string if no middle name)
- `getLastName(content: str) -> str`: Extract last name
- `getFirstAndLastName(content: str) -> list`: Extract first and last name as [first, last]
- `getFirstMiddleLastName(content: str) -> list`: Extract all parts as [first, middle, last]

## Cleaning Pipeline

The library applies the following cleaning steps in order:

1. **RemoveSpecialCharacters**: Removes periods (.)
2. **RemoveAfterComma**: Removes everything after the first comma
3. **RemoveIgnoreHeadLine**: Removes common titles, suffixes, and professional designations
4. **RemovePunctuation**: Removes content within parentheses, brackets, and braces
5. **RemoveExtraEnds**: Removes LinkedIn-style suffixes (• 1st, • 2nd, • 3rd+)
6. **ConvertSpanishToEnglish**: Converts international characters to ASCII equivalents
7. **RemoveUnEnglish** (optional): Removes non-English characters
8. **RemoveExtraSpace**: Trims whitespace

## Examples

See the [examples](examples/) directory for more comprehensive examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

deng-peng

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/deng-peng/people-name-cleaner/issues).
