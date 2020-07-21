class TestResult:

    def __init__(self, threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime, totalResponseDuration, isSuccess):
        self.threadId = threadId
        self.threadStartTime = threadStartTime
        self.threadEndTime = threadEndTime
        self.requestStarTime = requestStartTime
        self.requestEndTime = requestEndTime
        self.totalResponseDuration = totalResponseDuration
        self.isSuccess = isSuccess




