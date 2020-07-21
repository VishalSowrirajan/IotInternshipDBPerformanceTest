from abc import ABC, abstractmethod
from tester import TestResult


class AbstractDbTestJob(ABC):
    @abstractmethod
    def performReadTest(self, threadId):
        return TestResult

    @abstractmethod
    def performWriteTest(self, threadId):
        return TestResult

    @abstractmethod
    def performReadWithConditionTest(self, threadId):
        return TestResult
