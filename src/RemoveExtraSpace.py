import string

from IFullNameCleaner import IFullNameCleaner


class RemoveExtraSpace(IFullNameCleaner):

    def getCleanFullName(self, content: string):
        if not content:
            return content
        res = content.strip()
        return res
