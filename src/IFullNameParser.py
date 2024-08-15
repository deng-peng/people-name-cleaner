import string
from abc import ABCMeta, abstractmethod

class IFullNameParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getFirstMiddleLastName(self, content: string):
        pass

    @abstractmethod
    def getFirstAndLastName(self, content: string):
        pass

    @abstractmethod
    def getFirstName(self, content: string):
        pass

    @abstractmethod
    def getMiddleName(self, content: string):
        pass

    @abstractmethod
    def getLastName(self, content: string):
        pass
