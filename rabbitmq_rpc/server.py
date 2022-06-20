from rabbitmq_rpc import server as Server

server = Server.RPCServer(queue_name='default',
                          amqp_url="amqp://guest:guest@localhost:5672/",
                          threaded=False)

@server.consumer()
def add(a, b):
    return a+b

@server.consumer()
def plus(a, b):
    return a-b

if __name__ == "__main__":
    server.run()
