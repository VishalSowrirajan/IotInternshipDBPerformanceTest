import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.ticker as ticker


class DbResultPlot:

    def dbReadResultPlot(self):
        influxReadResults = pd.read_csv('read_influx.csvutil', usecols=[3, 5])
        influxResponseTime = influxReadResults.requestStartTime
        influxTimeDiff = influxReadResults.totalResponseDuration
        postgresTimeDiff= pd.read_csv('read_postgres.csvutil', usecols=[5])
        mongoTimeDiff = pd.read_csv('read_mongo.csvutil', usecols=[5])
        cassandraTimeDiff = pd.read_csv('read_cassandra.csvutil', usecols=[5])

        x_axis = [datetime.datetime.fromtimestamp(responseTime).strftime('%Y-%m-%d %H:%M:%S.%f') for responseTime in influxResponseTime]
        tick_spacing = 30
        fig, ax = plt.subplots(figsize=(20, 10))
        fig.suptitle('Database Select Query Evaluation', fontsize=20)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.plot(x_axis, cassandraTimeDiff, 'b-', color='green', label='Cassandra Db')
        plt.plot(x_axis, postgresTimeDiff, 'b-', color='blue', label='Postgres Db')
        plt.plot(x_axis, mongoTimeDiff, 'b-', color='red', label='Mongo Db')
        plt.plot(x_axis, influxTimeDiff, 'b-', color='yellow', label='Influx Db')
        plt.legend(loc='best')
        plt.ylabel('Response Time', fontsize=18)
        plt.xlabel('Time', fontsize=16)
        plt.xticks(rotation=90)
        plt.show()

    def dbWriteResultPlot(self):
        influxReadResults = pd.read_csv('write_influx.csvutil', usecols=[3, 5])
        influxResponseTime = influxReadResults.requestStartTime
        influxTimeDiff = influxReadResults.totalResponseDuration
        postgresTimeDiff= pd.read_csv('write_postgres.csvutil', usecols=[5])
        mongoTimeDiff = pd.read_csv('write_mongo.csvutil', usecols=[5])
        cassandraTimeDiff = pd.read_csv('write_cassandra.csvutil', usecols=[5])

        x_axis = [datetime.datetime.fromtimestamp(responseTime).strftime('%Y-%m-%d %H:%M:%S.%f') for responseTime in influxResponseTime]
        tick_spacing = 30
        fig, ax = plt.subplots(figsize=(20, 10))
        fig.suptitle('Database Write Query Evaluation', fontsize=20)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.plot(x_axis, cassandraTimeDiff, 'b-', color='green', label='Cassandra Db')
        plt.plot(x_axis, postgresTimeDiff, 'b-', color='blue', label='Postgres Db')
        plt.plot(x_axis, mongoTimeDiff, 'b-', color='red', label='Mongo Db')
        plt.plot(x_axis, influxTimeDiff, 'b-', color='yellow', label='Influx Db')
        plt.legend(loc='best')
        plt.ylabel('Response Time', fontsize=18)
        plt.xlabel('Time', fontsize=16)
        plt.xticks(rotation=90)
        plt.show()

    def dbReadWithConditionResultPlot(self):
        influxReadResults = pd.read_csv('read_with_condition_influx.csvutil', usecols=[3, 5])
        influxResponseTime = influxReadResults.requestStartTime
        influxTimeDiff = influxReadResults.totalResponseDuration
        postgresTimeDiff= pd.read_csv('read_with_condition_postgres.csvutil', usecols=[5])
        mongoTimeDiff = pd.read_csv('read_with_condition_mongo.csvutil', usecols=[5])
        cassandraTimeDiff = pd.read_csv('read_with_condition_cassandra.csvutil', usecols=[5])

        x_axis = [datetime.datetime.fromtimestamp(responseTime).strftime('%Y-%m-%d %H:%M:%S.%f') for responseTime in influxResponseTime]
        tick_spacing = 30
        fig, ax = plt.subplots(figsize=(20, 10))
        fig.suptitle('Database Read with condition Evaluation', fontsize=20)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.plot(x_axis, cassandraTimeDiff, 'b-', color='green', label='Cassandra Db')
        plt.plot(x_axis, postgresTimeDiff, 'b-', color='blue', label='Postgres Db')
        plt.plot(x_axis, mongoTimeDiff, 'b-', color='red', label='Mongo Db')
        plt.plot(x_axis, influxTimeDiff, 'b-', color='yellow', label='Influx Db')
        plt.legend(loc='best')
        plt.ylabel('Response Time', fontsize=18)
        plt.xlabel('Time', fontsize=16)
        plt.xticks(rotation=90)
        plt.show()