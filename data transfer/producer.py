from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib
import time

if __name__ == '__main__':

    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud_lib.read_ccloud_config(config_file)

    # Create Producer instance
    producer = Producer({
        'bootstrap.servers': conf['bootstrap.servers'],
        'sasl.mechanisms': conf['sasl.mechanisms'],
        'security.protocol': conf['security.protocol'],
        'sasl.username': conf['sasl.username'],
        'sasl.password': conf['sasl.password'],
    })

    # Create topic if needed
    ccloud_lib.create_topic(conf, topic)

    delivered_records = 0


    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))


    input_file = open('bcsample.json', )
    json_decode = json.load(input_file)[:1000]
    for key, value in enumerate(json_decode):
        document = item

        # print(record_key)
        for field in document:
            record_key = field
            record_value = document[field]
            # print(field,"-",document[field])
            print("Producing record: {}\t{}".format(record_key, record_value))
            producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)
            # p.poll() serves delivery reports (on_delivery)
            # from previous produce() calls.
            producer.poll(0)
            time.sleep(0.25)

    producer.flush()

    print("{} messages were produced to topic {}!".format(delivered_records, topic))