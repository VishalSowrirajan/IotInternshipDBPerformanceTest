import random
import traceback
from cassandra.cluster import Cluster
import time
from cassandra.auth import PlainTextAuthProvider

from tester.AbstractDbTestJob import AbstractDbTestJob
from tester.TestResult import TestResult


class CassandraDbTest(AbstractDbTestJob):

    def __init__(self, cassandraDbConfiguration):
        self.cassandraDbConfiguration = cassandraDbConfiguration

    def performReadTest(self, threadId):

        threadStartTime = time.time()
        cluster = None

        try:
            requestStartTime = time.time()
            auth_provider = PlainTextAuthProvider(username=self.cassandraDbConfiguration.username,
                                                  password=self.cassandraDbConfiguration.password)
            cluster = Cluster(contact_points=self.cassandraDbConfiguration.contact_points, port=self.cassandraDbConfiguration.port,
                              auth_provider=auth_provider)
            session = cluster.connect()
            session.set_keyspace(self.cassandraDbConfiguration.keyspace)
            rows = session.execute(random.choice(self.cassandraDbConfiguration.readQuery))
            requestEndTime = time.time()
            isSuccess = True

        except Exception:

            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if cluster != None:
                cluster.shutdown()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)

    def performWriteTest(self, threadId):

        threadStartTime = time.time()
        cluster = None
        try:
            requestStartTime = time.time()
            auth_provider = PlainTextAuthProvider(username=self.cassandraDbConfiguration.username,
                                                  password=self.cassandraDbConfiguration.password)
            cluster = Cluster(contact_points=self.cassandraDbConfiguration.contact_points, port=self.cassandraDbConfiguration.port,
                              auth_provider= auth_provider)
            session = cluster.connect()
            session.set_keyspace(self.cassandraDbConfiguration.keyspace)
            rows = session.execute(random.choice(self.cassandraDbConfiguration.writeQuery))
            requestEndTime = time.time()
            isSuccess = True

        except Exception:

            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:
            if cluster != None:
                cluster.shutdown()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)

    def performReadWithConditionTest(self, threadId):

        threadStartTime = time.time()
        cluster = None
        try:
            requestStartTime = time.time()
            auth_provider = PlainTextAuthProvider(username=self.cassandraDbConfiguration.username,
                                                  password=self.cassandraDbConfiguration.password)
            cluster = Cluster(contact_points=self.cassandraDbConfiguration.contact_points,
                              port=self.cassandraDbConfiguration.port,
                              auth_provider=auth_provider)
            session = cluster.connect()
            session.set_keyspace('thingsboard')
            rows = session.execute(random.choice(self.cassandraDbConfiguration.readWithConditionQuery))
            requestEndTime = time.time()
            isSuccess = True

        except Exception:

            requestEndTime = time.time()
            isSuccess = False
            traceback.print_exc()

        finally:

            if cluster != None:
                cluster.shutdown()

        totalResponseDuration = requestEndTime - requestStartTime
        threadEndTime = time.time()
        return TestResult(threadId, threadStartTime, threadEndTime, requestStartTime, requestEndTime,
                          totalResponseDuration, isSuccess)