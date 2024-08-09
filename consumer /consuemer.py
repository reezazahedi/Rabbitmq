import pika
import time
import random

def on_message_received(ch, method, properties, body):
    processing_time = 1
    print(f"received: {body}. will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("finished processing the message")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print("starting consuming")

channel.start_consuming()
