import string

from IFullNameCleaner import IFullNameCleaner


class RemoveSpecialCharacters(IFullNameCleaner):
    def __init__(self):
        pass

    def getCleanFullName(self, content: string):
        point = '.'
        res = content.replace(point, '')
        return res

