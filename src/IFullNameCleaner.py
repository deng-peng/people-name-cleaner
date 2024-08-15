import string
from abc import ABCMeta, abstractmethod


class IFullNameCleaner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getCleanFullName(self, content: string):
        pass
