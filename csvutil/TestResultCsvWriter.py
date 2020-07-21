import csv


class TestResultCsvWriter:

    def writeToCsv(self, testResults, filepath):
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["threadId", "threadStartTime", "threadEndTime", "requestStartTime", "requestEndTime",
                             "totalResponseDuration", "isSuccess"])
            for testResult in testResults:
                writer.writerow([testResult.threadId, testResult.threadStartTime, testResult.threadEndTime,
                                 testResult.requestStarTime, testResult.requestEndTime, testResult.totalResponseDuration,
                                 testResult.isSuccess])
