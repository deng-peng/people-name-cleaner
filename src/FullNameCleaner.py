import string

from ConvertSpanishToEnglish import ConvertSpanishToEnglish
from RemoveExtraSpace import RemoveExtraSpace
from RemoveUnEnglish import RemoveUnEnglish
from RemoveAfterComma import RemoveAfterComma
from RemoveExtraEnds import RemoveExtraEnds
from RemoveIgnoreHeadLine import RemoveIgnoreHeadLine
from RemovePunctuation import RemovePunctuation
from RemoveSpecialCharacters import RemoveSpecialCharacters


class FullNameCleaner:
    isFilterEnglish = True

    def __init__(self):
        self.removeSpecialCharacters = RemoveSpecialCharacters()
        self.removeAfterComma = RemoveAfterComma()
        self.removeIgnoreHeadLine = RemoveIgnoreHeadLine()
        self.removePunctuation = RemovePunctuation()
        self.removeExtraEnds = RemoveExtraEnds()
        self.convertSpanishToEnglish = ConvertSpanishToEnglish()
        self.removeUnEnglish = RemoveUnEnglish()
        self.removeExtraSpace = RemoveExtraSpace()

    def setFilterEnglist(self, isFilterEnglish: bool):
        self.isFilterEnglish = isFilterEnglish

    def getCleanFullName(self, content: string):
        if not content:
            return content
        res = content
        res = self.removeSpecialCharacters.getCleanFullName(res)
        res = self.removeAfterComma.getCleanFullName(res)
        res = self.removeIgnoreHeadLine.getCleanFullName(res)
        res = self.removePunctuation.getCleanFullName(res)
        res = self.removeExtraEnds.getCleanFullName(res)
        res = self.convertSpanishToEnglish.getCleanFullName(res)
        if self.isFilterEnglish:
            res = self.removeUnEnglish.getCleanFullName(res)
        res = self.removeExtraSpace.getCleanFullName(res)
        return res


if __name__ == '__main__':
    cleaner = FullNameCleaner()
    cleaner.setFilterEnglist(False)
    tempFullName1 = 'francisco jiménez garcía'
    firstAndLast = cleaner.getCleanFullName(tempFullName1)
    # 'francisco jimenez garcia'
    print(firstAndLast)

    tempFullName1 = 'bill gates, CEO, PHD'
    firstAndLast = cleaner.getCleanFullName(tempFullName1)
    # 'francisco jimenez garcia'
    print(firstAndLast)

    tempFullName1 = 'Joel R. Quinn, PMP'
    firstAndLast = cleaner.getCleanFullName(tempFullName1)
    # 'francisco jimenez garcia'
    print(firstAndLast)

    tempFullName1 = 'Joel 123 R. Quinn, PMP'
    firstAndLast = cleaner.getCleanFullName(tempFullName1)
    # 'francisco jimenez garcia'
    print(firstAndLast)

