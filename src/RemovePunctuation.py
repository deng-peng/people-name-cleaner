import re
import string

from IFullNameCleaner import IFullNameCleaner


class RemovePunctuation(IFullNameCleaner):
    def __init__(self):
        pass

    def getCleanFullName(self, content: string):
        res = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", content)
        return res
