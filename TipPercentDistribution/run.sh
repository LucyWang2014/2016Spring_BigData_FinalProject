hadoop jar /opt/cloudera/parcels/CDH-5.4.5-1.cdh5.4.5.p0.7/jars/hadoop-streaming-2.6.0-cdh5.4.5.jar \
    -D mapreduce.job.reduces=10 \
    -files map.py,reduce.py \
    -mapper map.py \
    -reducer reduce.py \
    -input raw_region \
    -output raw_tipPercDist
