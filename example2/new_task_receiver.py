import pika
import time

# create broker object
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
# connect for existing queue (if ir was created before we just connect)
channel.queue_declare(queue='task_queue1', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    body = str(body)
    time.sleep(body.count('.'))
    # manual message receiving acception
    # подтверждаем обработку сообщения обработчиком
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" [x] Done")


# равномерно распределяет сообщения в зависимости от нагрузки обработчиков
# смотрит на то, какой обработчик свободен, направляя ему сообщение
# если он еще не подтвердил выполнение задачи(не отправил basic_ack), не дает ему сообщение
# изменяет логику, по которой сообщения отдаются по порядку
channel.basic_qos(prefetch_count=1)
channel.basic_consume('task_queue1', callback, auto_ack=False)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
