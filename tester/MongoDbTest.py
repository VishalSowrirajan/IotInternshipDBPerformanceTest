import datetime
import random
import traceback

from pymongo import MongoClient
import time

from tester.AbstractDbTestJob import AbstractDbTestJob
from tester.TestResult import TestResult


class MongoDbTest(AbstractDbTestJob):
    def __init__(self, mongoDbConfiguration):
        self.mongoDbConfiguration = mongoDbConfiguration


    def performReadTest(self, threadId):
        threadStartTime = time.time()
        client = None

        try:
            requestStartTime = time.time()

            client = MongoClient(host=self.mongoDbConfiguration.host, port=self.mongoDbConfiguration.port,
                                 username=self.mongoDbConfiguration.username, password=self.mongoDbConfiguration.password)
            database = client.get_database(self.mongoDbConfiguration.databaseName)
            collections = database.get_collection(self.mongoDbConfiguration.collectionName)
            database.collections.find({})
            requestEndTime = time.time()
            isSuccess = True

        except Exception:
            requestEndTime = time.time()
            traceback.print_exc()
            isSuccess = False

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
        try:
            requestStartTime = time.time()
            insertData = random.choice(self.mongoDbConfiguration.writeQuery)
            #insertData['acc_timestamp'] = datetime.datetime.utcnow()
            insertData = {"acc_x": "10", "acc_y": "40", "acc_z": "18",
                   "acc_timestamp": datetime.datetime.utcnow()}
            client = MongoClient(host=self.mongoDbConfiguration.host, port=self.mongoDbConfiguration.port,
                                 username=self.mongoDbConfiguration.username, password=self.mongoDbConfiguration.password)
            database = client.get_database(self.mongoDbConfiguration.databaseName)
            collection = database.get_collection(self.mongoDbConfiguration.collectionName)
            mongoDbInsertQuery = collection.insert(insertData)
            requestEndTime = time.time()
            isSuccess = True

        except Exception:
            requestEndTime = time.time()
            traceback.print_exc()
            isSuccess = False

        finally:
            if client != None:
                client.close()
            totalResponseDuration = requestEndTime - requestStartTime
            threadEndTime = time.time()
            return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                              totalResponseDuration, isSuccess)

    def performReadWithConditionTest(self, threadId):

        threadStartTime = time.time()
        client = None

        try:
            requestStartTime = time.time()
            readWithConditionData = random.choice(self.mongoDbConfiguration.readWithConditionQuery)
            client = MongoClient(host=self.mongoDbConfiguration.host, port=self.mongoDbConfiguration.port,
                                 username=self.mongoDbConfiguration.username, password=self.mongoDbConfiguration.password)
            database = client.get_database(self.mongoDbConfiguration.databaseName)
            collection = database.get_collection(self.mongoDbConfiguration.collectionName)
            database.test1.find(readWithConditionData)
            requestEndTime = time.time()
            isSuccess = True

        except Exception:
            requestEndTime = time.time()
            traceback.print_exc()
            isSuccess = False

        finally:
            if client != None:
                client.close()
            totalResponseDuration = requestEndTime - requestStartTime
            threadEndTime = time.time()
            return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                              totalResponseDuration, isSuccess)