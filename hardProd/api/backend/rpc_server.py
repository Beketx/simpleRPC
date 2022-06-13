import pika

# Ustanovka soednineniya
connection_params = pika.ConnectionParameters(host='localhost')
# Async to sync for read or write block till we get response from queue
connection = pika.BlockingConnection(connection_params)
# Zdes proisodit vzaimodeistvie s queueu (ocheredu) and realise all methods of amqp.
# By channel we communicate with ampq queue
channel = connection.channel()
# Creatig or checking queue queue=queue_name
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n < 3:
        return 1
    i = 3
    last1 = 1
    last2 = 1
    while i <= n:
        result = last1 + last2
        last2 = last1
        last1 = result
        i += 1
    return result

def on_request(ch, method, props, body):
    """
    Exchange eto pochtovy yawik kuda kladut vse message, a on uje raspredelyaet ochered
    """
    n = int(body)

    func = props.headers.get('api')
    print(func)
    # locals()['myFunc']()
    # globals()['myFunc2']()
    response = eval(str(func))
    # response = fib(n)
    print(response)
    # print(123)
    # otpravka soobwenie
    ch.basic_publish(exchange='', # name of tochki obmena , v kotoruy my otpravlyaem soobwenie
                     routing_key=props.reply_to, # key of morshrutization, s kotorym budet opublikovana v tochku obmena
                     properties=pika.BasicProperties(correlation_id = props.correlation_id), # delivery_mode = 2 # make message persistant
                     body=str(response)) # text of our message, kotoruy my otpravlyaem v ochered
    # pootverzhdaem brokeru chto soobwenie polucheno and soobwenie budet udaleno iz ocheredi
    ch.basic_ack(delivery_tag=method.delivery_tag)

# poluchenie soobweniya
# no_ack = True, ne nujno rukami potverzhdat soobwenie, v function obrabotwike
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
# Zakrivaem soedineniya
channel.start_consuming()