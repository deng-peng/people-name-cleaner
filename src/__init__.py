"""
People Name Cleaner
A Python library for cleaning and parsing people's names from various formats
"""

from .FullNameCleaner import FullNameCleaner
from .FullNameParser import FullNameParser
from .IFullNameCleaner import IFullNameCleaner
from .IFullNameParser import IFullNameParser

__all__ = [
    'FullNameCleaner',
    'FullNameParser',
    'IFullNameCleaner',
    'IFullNameParser',
]

__version__ = '1.0.0'
