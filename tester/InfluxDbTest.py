import random
import traceback
import pytz
import datetime
import time
from tester.AbstractDbTestJob import AbstractDbTestJob
from tester.TestResult import TestResult
from influxdb import InfluxDBClient

class InfluxDbTest(AbstractDbTestJob):

    def __init__(self, influxDbConfiguration):
        self.influxDbConfiguration = influxDbConfiguration


    def performReadTest(self, threadId):

        threadStartTime = time.time()
        client = None
        requestStartTime = None
        requestEndTime = None
        totalResponseDuration = None

        try:
            requestStartTime = time.time()
            client = InfluxDBClient(host=self.influxDbConfiguration.host, port=self.influxDbConfiguration.port,
                                    username=self.influxDbConfiguration.username, password=self.influxDbConfiguration.password)
            client.switch_database(self.influxDbConfiguration.databaseName)
            client.query(self.influxDbConfiguration.readQuery)
            requestEndTime = time.time()
            isSuccess = True

        except Exception as error:
            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if client != None:
                client.close()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)

    def performWriteTest(self, threadId):

        threadStartTime = time.time()
        client = None
        requestStartTime = None
        requestEndTime = None
        totalResponseDuration = None

        try:
            dateTime = datetime.datetime.utcnow()
            dateTime_with_timezone = dateTime.replace(tzinfo=pytz.UTC)
            timeStamp = dateTime_with_timezone.isoformat()
            chosen_query = random.choice(self.influxDbConfiguration.writeQuery)
            inputInfluxDb = [
                {
                    "measurement": chosen_query["measurement"],
                    "tags": chosen_query["tags"],
                    "fields": chosen_query["fields"],
                    "time": timeStamp}
            ]
            requestStartTime = time.time()
            client = InfluxDBClient(host=self.influxDbConfiguration.host, port=self.influxDbConfiguration.port,
                                    username=self.influxDbConfiguration.username, password=self.influxDbConfiguration.password,
                                    database=self.influxDbConfiguration.databaseName)
            client.switch_database(self.influxDbConfiguration.databaseName)
            client.write_points(inputInfluxDb)
            requestEndTime = time.time()
            isSuccess = True

        except Exception:

            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if client != None:
                client.close()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)

    def performReadWithConditionTest(self, threadId):
        client = None
        threadStartTime = time.time()
        requestStartTime = None
        requestEndTime = None
        totalResponseDuration = None
        readQuery = None
        readWithConditionQuery = None
        writeQuery = None

        try:
            requestStartTime = time.time()
            client = InfluxDBClient(host=self.influxDbConfiguration.host, port=self.influxDbConfiguration.port,
                                    username=self.influxDbConfiguration.username,
                                    password=self.influxDbConfiguration.password,
                                    database=self.influxDbConfiguration.databaseName)
            client.switch_database(self.influxDbConfiguration.databaseName)
            client.query(random.choice(self.influxDbConfiguration.readWithConditionQuery))
            requestEndTime = time.time()
            isSuccess = True

        except Exception:
            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if client != None:
                client.close()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)