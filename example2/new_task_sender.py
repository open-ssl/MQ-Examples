import sys
import pika

message = ' '.join(sys.argv[1:]) or "Hello World!"
# create broker object
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue for sending message
# durable=True means that we don't lose out message if server will fail
channel.queue_declare(queue='task_queue1', durable=True)

# do public
channel.basic_publish(exchange='',
                      routing_key='task_queue1',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # очередь не потеряется при сбое
                      ))

print(" [x] Sent %r" % (message, ))
# safety connection ending
connection.close()
