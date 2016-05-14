from pyspark import SparkContext

#dataFile = "data.txt"  # Should be some file on your system

#if the key has / in it, calling spark-submit wouldn't work
        
AWS_Secret_Key_ID = "AKIAJUQVKHBZYYV3L6VA"        
AWS_Secret_Access_Key = "F+xDZTvIASS1AecgnD8jzg53Fha5TYBtYypFJMmV"
bucket = "bigdata-proj"
prefix_trip = "raw_data/trip_data/*.csv"
prefix_fares = "raw_data/fare_data/*.csv"
#filename = "s3n://${ID}:{SECRET}@${BUCKET}/${Path}".format({})

filename_trip = "s3n://{}:{}@{}/{}".format(AWS_Secret_Key_ID, AWS_Secret_Access_Key, bucket, prefix_trip)
filename_fares = "s3n://{}:{}@{}/{}".format(AWS_Secret_Key_ID, AWS_Secret_Access_Key, bucket, prefix_fares)



sc = SparkContext("local", "test merge trip fare")
"""
config_dict = {"fs.s3n.awsAccessKeyId":"AKIAJXRJ75OTCK7KWT2A",
               "fs.s3n.awsSecretAccessKey":"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"}
logData = sc.hadoopFile(filename,
                    'org.apache.hadoop.mapred.TextInputFormat',
                    'org.apache.hadoop.io.Text',
                    'org.apache.hadoop.io.LongWritable',
                    conf=config_dict)
"""
logData_trips = sc.textFile(filename_trips).cache()
logData_fares = sc.textFile(filename_fares).cache()

trips = logData_trips.first()
fares = logData_fares.first()

print("First line of trips: %" %(trips))
print("First line of fares: %" % (fares))