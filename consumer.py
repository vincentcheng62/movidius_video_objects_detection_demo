from kafka import KafkaConsumer
import json
import msgpack

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('mwc_camera_info', group_id=None,
                         bootstrap_servers=['172.18.6.120:31090'], consumer_timeout_ms=1000, auto_offset_reset='earliest', enable_auto_commit=False)
#for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
   # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                      message.offset, message.key,
     #                                     message.value))
 #   print(message)


# consume earliest available messages, don't commit offsets
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
#consumer2 = KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))
#for msg in consumer2:
#    print(msg)

# consume msgpack
#KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
#KafkaConsumer(consumer_timeout_ms=1000)

for msg in consumer:
    print(msg)
# Subscribe to a regex topic pattern
#consumer = KafkaConsumer()
#consumer.subscribe(pattern='^awesome.*')

# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
#consumer1 = KafkaConsumer('my-topic',
#                          group_id='my-group',
#                          bootstrap_servers='my.server.com')
#consumer2 = KafkaConsumer('my-topic',
#                          group_id='my-group',
#                          bootstrap_servers='my.server.com')
consumer.close()
