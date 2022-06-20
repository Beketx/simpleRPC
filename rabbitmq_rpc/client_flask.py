from rabbitmq_rpc.client import RPCClient
import flask
web = flask.Flask(__name__)
web.debug = True
import time

def add(i):
    t1 = time.time()
    client = RPCClient(amqp_url='amqp://guest:guest@localhost:5672/', queue_name="default")
    # return 2
    client.connect()
    res = client.call_add(0, i)
    t2 = time.time()
    print(f"{0} + {i} = {res} RPC Time Cost: {t2-t1:.2f}")
    return t2

@web.route('/web/<n>')
def test_web(n):
    res = add(int(n))
    return str(res)
if __name__ == '__main__':
    # Notice, In default, flask enabled threading.
    # If single-thread is needed, pass in 'threaded=False' option
    web.run(host = '0.0.0.0', use_reloader = False)
