import random
import traceback
import psycopg2
import time
from tester.AbstractDbTestJob import AbstractDbTestJob
from tester.TestResult import TestResult


class PostgresDbTest(AbstractDbTestJob):

    def __init__(self, postgresDbConfiguration):
        self.postgresDbConfiguration = postgresDbConfiguration

    def performReadTest(self, threadId):
        threadStartTime = time.time()
        connection = None

        try:
            requestStartTime = time.time()
            connection = psycopg2.connect(user=self.postgresDbConfiguration.username,
                                          password=self.postgresDbConfiguration.password,
                                          host=self.postgresDbConfiguration.host,
                                          port=self.postgresDbConfiguration.port,
                                          database=self.postgresDbConfiguration.databaseName)
            cursor = connection.cursor()
            postgreReadQuery = random.choice(self.postgresDbConfiguration.readQuery)
            cursor.execute(postgreReadQuery)
            connection.commit()
            requestEndTime = time.time()
            isSuccess = True
            print(threadId)

        except (Exception, psycopg2.Error):
            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if (connection):
                connection.close()
            totalResponseDuration = requestEndTime - requestStartTime
            threadEndTime = time.time()
            return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                              totalResponseDuration, isSuccess)

    def performWriteTest(self, threadId):

        threadStartTime = time.time()
        connection = None

        try:
            requestStartTime = time.time()
            connection = psycopg2.connect(user=self.postgresDbConfiguration.username,
                                          password=self.postgresDbConfiguration.password,
                                          host=self.postgresDbConfiguration.host,
                                          port=self.postgresDbConfiguration.port,
                                          database=self.postgresDbConfiguration.databaseName)
            cursor = connection.cursor()
            postgreInsertQuery = random.choice(self.postgresDbConfiguration.writeQuery)
            cursor.execute(postgreInsertQuery)
            connection.commit()
            requestEndTime = time.time()
            isSuccess = True

        except (Exception, psycopg2.Error):
            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if(connection):
                connection.close()
            totalResponseDuration = requestEndTime - requestStartTime
            threadEndTime = time.time()
            return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                              totalResponseDuration, isSuccess)

    def performReadWithConditionTest(self, threadId):

        threadStartTime = time.time()
        connection = None

        try:
            requestStartTime = time.time()
            connection = psycopg2.connect(user=self.postgresDbConfiguration.username,
                                          password=self.postgresDbConfiguration.password,
                                          host=self.postgresDbConfiguration.host,
                                          port=self.postgresDbConfiguration.port,
                                          database=self.postgresDbConfiguration.databaseName)
            cursor = connection.cursor()
            postgreReadWithConditionQuery = random.choice(self.postgresDbConfiguration.readWithConditionQuery)
            cursor.execute(postgreReadWithConditionQuery)
            connection.commit()
            requestEndTime = time.time()
            isSuccess = True

        except (Exception, psycopg2.Error):
            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if(connection):
                connection.close()
            totalResponseDuration = requestEndTime - requestStartTime
            threadEndTime = time.time()
            return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                              totalResponseDuration, isSuccess)