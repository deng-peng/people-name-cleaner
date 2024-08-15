import string

from IFullNameCleaner import IFullNameCleaner


class RemoveExtraEnds(IFullNameCleaner):
    def __init__(self):
        self.ends = ['• 1st', '• 2nd', '• 3rd+'];

    def getCleanFullName(self, content: string):
        res = content
        for end in self.ends:
            if content.endswith(end):
                res = content[0:len(content) - len(end)]
                break
        if len(res) > 0:
            res = res.rstrip()
        return res
