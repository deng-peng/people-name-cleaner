import string

from unidecode import unidecode

from IFullNameCleaner import IFullNameCleaner


class ConvertSpanishToEnglish(IFullNameCleaner):

    def getCleanFullName(self, content: string):
        res = unidecode(content)
        return res
