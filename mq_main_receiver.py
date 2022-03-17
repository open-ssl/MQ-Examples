# library again)
import pika

# create broker object
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
# connect for existing queue (if ir was created before we just connect)
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))


channel.basic_consume('hello', callback, auto_ack=True)


print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
