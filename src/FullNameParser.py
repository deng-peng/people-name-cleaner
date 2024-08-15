import string

from FullNameCleaner import FullNameCleaner
from IFullNameParser import IFullNameParser


class FullNameParser(IFullNameParser):

    isFilterEnglish = False

    def __init__(self, fullNameCleaner: FullNameCleaner):
        self.fullNameCleaner = fullNameCleaner

    def setFilterEnglist(self, isFilterEnglish):
        self.isFilterEnglish = isFilterEnglish

    def getFirstMiddleLastName(self, content: string):
        return self.cleanAndSplitName(content)

    def getFirstAndLastName(self, content: string):
        return [self.cleanAndSplitName(content)[0], self.cleanAndSplitName(content)[2]]

    def getFirstName(self, content: string):
        return self.cleanAndSplitName(content)[0]

    def getMiddleName(self, content: string):
        return self.cleanAndSplitName(content)[1]

    def getLastName(self, content: string):
        return self.cleanAndSplitName(content)[2]

    def cleanAndSplitName(self, content: string):
        self.fullNameCleaner.setFilterEnglist(self.isFilterEnglish)
        filterContent = self.fullNameCleaner.getCleanFullName(content)
        res = ['', '', '']
        if not filterContent:
            return res
        listNames = filterContent.split(' ')
        if len(listNames) > 0:
            res[0] = listNames[0]
        if len(listNames) > 1:
            res[2] = listNames[len(listNames) - 1]
        if len(listNames) > 2:
            middleName = filterContent.replace(res[0], '')
            middleName = middleName.replace(res[2], '')
            if (middleName) :
                res[1] = middleName.strip()
        return res


if __name__ == '__main__':
    parser = FullNameParser(FullNameCleaner())
    tempFullName1 = 'francisco jiménez garcía'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    first = parser.getFirstName(tempFullName1)
    last = parser.getLastName(tempFullName1)
    # ['francisco', 'garcia']
    print(firstAndLast)

    tempFullName1 = 'daniela pilar caquimbo yustres'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['daniela', 'yustres']
    print(firstAndLast)

    tempFullName1 = 'aditya rawal'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['aditya', 'rawal']
    print(firstAndLast)

    tempFullName1 = 'thaddeus "matt" biagas'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['thaddeus', 'biagas']
    print(firstAndLast)

    tempFullName1 = '冯仰利'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['Feng', 'Li']
    print(firstAndLast)

    tempFullName1 = '旭 姚'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['Xu', 'Yao']
    print(firstAndLast)

    tempFullName1 = '현명 김'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['hyeonmyeong', 'gim']
    print(firstAndLast)

    tempFullName1 = 'олександра миляник'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['oleksandra', 'miljanik']
    print(firstAndLast)

    tempFullName1 = 'huệ trần'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['hu', 'tran']
    print(firstAndLast)

    tempFullName1 = 'mohammed abdul aziz syed ☁'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['mohammed', 'syed']
    print(firstAndLast)

    tempFullName1 = 'شيخة البنات  '
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['', '']
    print(firstAndLast)

    tempFullName1 = 'jisdsd sdfdfd cto (1231232131) • 2nd'
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['jisdsd', 'sdfdfd']
    print(firstAndLast)

    tempFullName1 = "'inoke • 2nd"
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['inoke', '']
    print(firstAndLast)

    tempFullName1 = "rob liu, ceo"
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['rob', 'liu']
    print(firstAndLast)

    tempFullName1 = "Dr. Ofla Herzog"
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['ofla', 'herzog']
    print(firstAndLast)

    tempFullName1 = "Felix Watson Jr."
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['felix', 'watson']
    print(firstAndLast)

    tempFullName1 = "Katie De Lala"
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['katie', 'de lala']
    print(firstAndLast)

    tempFullName1 = "Katie Van Der Lala"
    firstAndLast = parser.getFirstAndLastName(tempFullName1)
    # ['katie', 'van der lala']
    print(firstAndLast)

    tempFullName1 = "Katie Della Lala"
    firstAndLast = parser.getFirstMiddleLastName(tempFullName1)
    # ['katie', 'della', 'lala']
    print(firstAndLast)

    tempFullName1 = "Katie Du Lala"
    firstAndLast = parser.getFirstMiddleLastName(tempFullName1)
    # ['katie', 'du', 'lala']
    print(firstAndLast)

    tempFullName1 = "mohammed al attar"
    firstAndLast = parser.getFirstMiddleLastName(tempFullName1)
    # ['mohammed', 'al', 'attar']
    print(firstAndLast)

    tempFullName1 = "Katie Du Lala"
    firstAndLast = parser.getFirstMiddleLastName(tempFullName1)
    # ['katie', 'du', 'lala']
    print(firstAndLast)
