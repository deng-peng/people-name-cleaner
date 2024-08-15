import string

from IFullNameCleaner import IFullNameCleaner


class RemoveAfterComma(IFullNameCleaner):

    def getCleanFullName(self, content: string):
        if not content:
            return content
        res = content
        comma = ','
        if comma in content:
            res = res.split(comma)[0];
        return res
