from rabbitmq_rpc.client import RPCClient
import time

def fack(i):
    t1 = time.time()
    client = RPCClient(amqp_url='amqp://guest:guest@localhost')
    res = client.call_add(0, i)
    res2 = client.call_plus(0, i)
    print(res2, "It's a plus function")
    t2= time.time()
    print(f"{0} + {i} = {res} RPC Time Cost: {t2-t1:.2f}")
    return res

if __name__ == "__main__":
    print(123)
    # t1 = time.time()
    client = RPCClient(amqp_url='amqp://guest:guest@localhost')
    res = client.call_add(0, 10)
    print(res)
    res2 = client.call_plus(0, 10)
    print(res2, "It's a plus function")
    print(f"{0} + {10} = {res} RPC Time Cost")
    print(res)
    # obj = add(15)
    # obj = add(20)



