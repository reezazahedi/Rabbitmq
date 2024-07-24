import pika
import time
import random

connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

messageId = 1

while(True):
    message = f"Sending messageId: {messageId}"

    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    print(f"send message: {message}")

    time.sleep(random.randint(1, 4))

    messageId+=1
    
