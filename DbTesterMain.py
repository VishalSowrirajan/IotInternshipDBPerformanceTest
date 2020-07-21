import time

from Visualization import Visualization
from config.ConfigParser import ConfigParser
from tester.CassandraDbTest import CassandraDbTest
from tester.InfluxDbTest import InfluxDbTest
from tester.MongoDbTest import MongoDbTest
from tester.PostgresDbTest import PostgresDbTest
import multiprocessing.dummy as mp
import sys
from csvutil.TestResultCsvWriter import TestResultCsvWriter


def main():
    #Command line argument
    filePath = sys.argv[1]
    poolSize = 50
    threadCount = 500
    threadSleepTime = 5

    #Configurations
    influxConfiguration = ConfigParser.parseInfluxDbConfig(filePath)
    cassandraConfiguration = ConfigParser.parseCassandraDbConfig(filePath)
    postgresConfiguration = ConfigParser.parsePostgresDbConfig(filePath)
    mongoConfiguration = ConfigParser.parseMongoDbConfig(filePath)

    influxDbTest = InfluxDbTest(influxConfiguration)
    cassandraDbTest = CassandraDbTest(cassandraConfiguration)
    postgresDbTest = PostgresDbTest(postgresConfiguration)
    mongoDbTest = MongoDbTest(mongoConfiguration)
    writerToCsv = TestResultCsvWriter()

    print("READ OPERATION STARTED")
    #INFLUX READ
    if influxConfiguration != None:
        pool = mp.Pool(poolSize)
        readInfluxPool = pool.map(influxDbTest.performReadTest, range(0, threadCount))
        pool.close()
        pool.join()
        writerToCsv.writeToCsv(readInfluxPool, "read_influx.csv")
        print("Influx read done")
    time.sleep(threadSleepTime)
    #CASSANDRA READ
    pool = mp.Pool(poolSize)
    readCassandraPool = pool.map(cassandraDbTest.performReadTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readCassandraPool, "read_cassandra.csv")
    print("Cassandra read done")
    time.sleep(threadSleepTime)
    #POSTGRES READ
    pool = mp.Pool(poolSize)
    readPostgresPool = pool.map(postgresDbTest.performReadTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readPostgresPool, "read_postgres.csv")
    print("Postgres read done")
    time.sleep(threadSleepTime)
    #MONGO READ
    pool = mp.Pool(poolSize)
    readMongoPool = pool.map(mongoDbTest.performReadTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readMongoPool, "read_mongo.csv")
    print("Mongo read done")
    time.sleep(threadSleepTime)

    print("WRITE OPERATIONS STARTED")

    pool = mp.Pool(poolSize)
    writeInfluxPool = pool.map(influxDbTest.performWriteTest, range(0, threadCount))
    pool.close()
    pool.join()
    time.sleep(threadSleepTime)
    writerToCsv.writeToCsv(writeInfluxPool, "write_influx.csv")
    print("Influx Db Write done")
    #CASSANDRA WRITE
    pool = mp.Pool(poolSize)
    writeCassandraPool = pool.map(cassandraDbTest.performWriteTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(writeCassandraPool, "write_cassandra.csv")
    time.sleep(threadSleepTime)
    print("Cassandra Db Write done")
    #POSTGRES WRITE
    pool = mp.Pool(poolSize)
    writePostgresPool = pool.map(postgresDbTest.performWriteTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(writePostgresPool, "write_postgres.csv")
    time.sleep(threadSleepTime)
    print("Postgres Db Write done")
    #MONGO DB
    pool = mp.Pool(poolSize)
    writeMongoPool = pool.map(mongoDbTest.performWriteTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(writeMongoPool, "write_mongo.csv")
    time.sleep(threadSleepTime)
    print("Mongo Db Write done")

    #SELECT WITH CONDITION
    #INFLUX
    pool = mp.Pool(poolSize)
    readInfluxWithConditionPool = pool.map(influxDbTest.performReadWithConditionTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readInfluxWithConditionPool, "read_with_condition_influx.csv")
    print("Influx Db Read With condition done")
    time.sleep(threadSleepTime)
    #CASSANDRA
    pool = mp.Pool(poolSize)
    readCassandraWithConditionPool = pool.map(cassandraDbTest.performReadWithConditionTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readCassandraWithConditionPool, "read_with_condition_cassandra.csv")
    print("Cassandra Db Read With condition done")
    time.sleep(threadSleepTime)
    #POSTGRES
    pool = mp.Pool(poolSize)
    readPostgresWithConditionPool = pool.map(postgresDbTest.performReadWithConditionTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readPostgresWithConditionPool, "read_with_condition_postgres.csv")
    print("Postgres Db Read With condition done")
    time.sleep(threadSleepTime)
    #MONGO
    pool = mp.Pool(poolSize)
    readMongoWithConditionPool = pool.map(mongoDbTest.performReadWithConditionTest, range(0, threadCount))
    pool.close()
    pool.join()
    writerToCsv.writeToCsv(readMongoWithConditionPool, "read_with_condition_mongo.csv")
    print("Mongo Db Read With condition done")

    visualization = Visualization()
    visualization.dbReadResultPlot()
    visualization.dbWriteResultPlot()
    visualization.dbReadWithConditionResultPlot()

if __name__ == "__main__":
    sys.argv[1]
    main()

