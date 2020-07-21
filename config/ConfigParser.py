import json
from config.CassandraDbConfiguration import CassandraDbConfiguration
from config.InfluxDbConfiguration import InfluxDbConfiguration
from config.MongoDbConfiguration import MongoDbConfiguration
from config.PostgresDbConfigurtion import PostgresDbConfiguration


class ConfigParser:

    @staticmethod
    def parseMongoDbConfig(filepath):
        mongoDbConfiguration = None
        with open(filepath, "r") as read_file:
            configData = json.load(read_file)
            mongoConfigData = configData["mongoDb"]
            if mongoConfigData != None:
                mongoDbConfiguration = MongoDbConfiguration()
                mongoHost = mongoConfigData['host']
                mongoDbConfiguration.host = mongoHost
                mongoPort = mongoConfigData['port']
                mongoDbConfiguration.port = mongoPort
                mongoUsername = mongoConfigData['username']
                mongoDbConfiguration.username = mongoUsername
                mongoPassword = mongoConfigData['password']
                mongoDbConfiguration.password = mongoPassword
                mongoDatabaseName = mongoConfigData['databaseName']
                mongoDbConfiguration.databaseName = mongoDatabaseName
                mongoCollection = mongoConfigData['collection']
                mongoDbConfiguration.collectionName = mongoCollection
                mongoReadWithConditionQuery = mongoConfigData['readWithConditionQuery']
                mongoDbConfiguration.readWithConditionQuery = mongoReadWithConditionQuery
                mongoWriteQuery = mongoConfigData['writeQuery']
                mongoDbConfiguration.writeQuery = mongoWriteQuery

        return mongoDbConfiguration

    @staticmethod
    def parsePostgresDbConfig(filepath):
        postgresDbConfiguration = None
        with open(filepath, "r") as read_file:
            configData = json.load(read_file)
            postgresConfigData = configData["postgresDb"]
            if postgresConfigData != None:
                postgresDbConfiguration = PostgresDbConfiguration()
                postgresHost = postgresConfigData['host']
                postgresDbConfiguration.host = postgresHost
                postgresPort = postgresConfigData['port']
                postgresDbConfiguration.port = postgresPort
                postgresUsername = postgresConfigData['username']
                postgresDbConfiguration.username = postgresUsername
                postgresPassword = postgresConfigData['password']
                postgresDbConfiguration.password = postgresPassword
                postgresDatabaseName = postgresConfigData['databaseName']
                postgresDbConfiguration.databaseName = postgresDatabaseName
                postgresReadWithConditionQuery = postgresConfigData['readWithConditionQuery']
                postgresDbConfiguration.readWithConditionQuery = postgresReadWithConditionQuery
                postgresWriteQuery = postgresConfigData['writeQuery']
                postgresDbConfiguration.writeQuery = postgresWriteQuery
                postgresReadQuery = postgresConfigData['readQuery']
                postgresDbConfiguration.readQuery = postgresReadQuery

        return postgresDbConfiguration

    @staticmethod
    def parseCassandraDbConfig(filepath):
        cassandraDbConfiguration = None
        with open(filepath, "r") as read_file:
            configData = json.load(read_file)
            cassandraConfigData = configData["cassandraDb"]
            if cassandraConfigData != None:
                cassandraDbConfiguration = CassandraDbConfiguration()
                cassandraContactPoints = cassandraConfigData['contact_points']
                cassandraDbConfiguration.contact_points = cassandraContactPoints
                cassandraPort = cassandraConfigData['port']
                cassandraDbConfiguration.port = cassandraPort
                cassandraUsername = cassandraConfigData['username']
                cassandraDbConfiguration.username = cassandraUsername
                cassandraPassword = cassandraConfigData['password']
                cassandraDbConfiguration.password = cassandraPassword
                cassandraKeyspace = cassandraConfigData['keyspace']
                cassandraDbConfiguration.keyspace = cassandraKeyspace
                cassandraReadWithConditionQuery = cassandraConfigData['readWithConditionQuery']
                cassandraDbConfiguration.readWithConditionQuery = cassandraReadWithConditionQuery
                cassandraWriteQuery = cassandraConfigData['writeQuery']
                cassandraDbConfiguration.writeQuery = cassandraWriteQuery
                cassandraReadQuery = cassandraConfigData['readQuery']
                cassandraDbConfiguration.readQuery = cassandraReadQuery


        return cassandraDbConfiguration

    @staticmethod
    def parseInfluxDbConfig(filepath):
        influxDbConfiguration = None
        with open(filepath, "r") as read_file:
            configData = json.load(read_file)
            influxConfigData = configData["influxDb"]

            if influxConfigData != None:
                influxDbConfiguration = InfluxDbConfiguration()
                influxHost = influxConfigData['host']
                influxDbConfiguration.host = influxHost
                influxPort = influxConfigData['port']
                influxDbConfiguration.port = influxPort
                influxUsername = influxConfigData['username']
                influxDbConfiguration.username = influxUsername
                influxPassword = influxConfigData['password']
                influxDbConfiguration.password = influxPassword
                influxDatabaseName = influxConfigData['databaseName']
                influxDbConfiguration.databaseName = influxDatabaseName
                influxReadWithConditionQuery = influxConfigData['readWithConditionQuery']
                influxDbConfiguration.readWithConditionQuery = influxReadWithConditionQuery
                influxWriteQuery = influxConfigData['writeQuery']
                influxDbConfiguration.writeQuery = influxWriteQuery
                influxReadQuery = influxConfigData['readQuery']
                influxDbConfiguration.readQuery = influxReadQuery

        return influxDbConfiguration

