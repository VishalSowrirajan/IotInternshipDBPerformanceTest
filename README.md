***************** WELCOME TO DPSS IOT SENSORS STREAM - DPSS INTERNSHIP 2019 ********************

This project aims to compare three Open source IoT servers based on the performance of Database
and Communication protocol performance.
The python script intends to evaluate the performance of the Databases namely Cassandra DB, Mongo DB,
Postgres DB, Elastic DB and Influx DB.

The performance result for **Read** query performance:
![ReadPlot](DB Read.png)

The performance result for **Write** query performance:
![WritePlot](Write Query.png)
![Test Image 2](“Write Query.png”)

The performance result for **Read With Condition** query performance:
![ReadWithConditionPlot](Read With Condition Query.png)

Run the following command to install the required dependencies:
python setup.py install

Once the dependencies are installed, run the following command from command line to run the dbTester App:
(The filepath indicates the path where input JSON file is stored)
python DbTester.py filepath

JSON DATA:
    - The format of the json should me maintained as JSON is designed as per the code structure
    - For Influx db data, DO NOT PROVIDE the timestamp value as the timestamp is manually handled in the code for database evaluation.
    - Multiple queries are required to avoid query caching issue. 
    
Once the DbTester app is run, csv files will be generated for READ, WRITE and READ_WITH_CONDITIONS with threadId, thread start and
end time, request start and end time, total time duration for the request and the success rate of the threads.

Once the csv files are generated, the visualization is done eventually in the code 
and the read, write and read with condition plots are displayed.

If dependencies aren't download, please try the following in the terminal
pip install psycopg2;
pip install pandas;
pip install matplotlib;
pip install cassandra-driver;
pip install pymongo;
pip install influxdb

********************** END **********************


