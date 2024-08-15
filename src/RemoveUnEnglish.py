import re
import string

from IFullNameCleaner import IFullNameCleaner


class RemoveUnEnglish(IFullNameCleaner):
    def __init__(self):
        pass

    def getCleanFullName(self, content: string):
        res = re.sub("[^A-Za-z0-9.\- ]", '', content)
        return res
