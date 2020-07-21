from setuptools import setup

setup(
    name='DbTester',
    version='1.0',
    packages=['cassandra-driver', 'psycopg2', 'pymongo', 'influxdb', 'pytz'],
    author='Sarangan Gnanasegaram, Vishal Sowrirajan, Vinoth Kumar Adusumilli Govindarajulu, '
           'Ashwin Vasudevan Chinthu, Rine Rajendran',
    author_email='gnans01@ads.uni-passau.de,sowrir01@ads.uni-passau.de, adusum01@ads.uni-passau.de, '
                 'chinth01@ads.uni-passau.de,'
                 ' rajend05@ads.uni-passau.de',
    description='DPSS SS19 project - University of Passau', install_requires=['influxdb', 'pytz', 'pymongo', 'bson',
                                                                              'cassandra'])

