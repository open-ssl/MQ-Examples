# library with amqp protocol logic
import pika

# create broker object
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue for sending message
channel.queue_declare(queue='hello')

# do public
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

# safety connection ending
connection.close()
