from fastapi import APIRouter
from api.api_models import Data, SessionStatus
from api.backend.rpc_client import FibonacciRpcClient

router = APIRouter()

@router.get('/')
def test():
    return 'API is running'

@router.post('/calculate')
def calculate_fibonacci(inputData:Data):
    fibonacci_rpc = FibonacciRpcClient()

    print(" [x] Requesting fib(%s)" % inputData.fibNumber)
    response = fibonacci_rpc.call(inputData.fibNumber)
    print(" [.] Got %r" % response)

    return response

@router.post('/create_session')
def calculate_fibonacci(data:SessionStatus):
    fibonacci_rpc = FibonacciRpcClient()

    print(" [x] Requesting fib(%s)" % data)
    response = fibonacci_rpc.call_create_session(data)
    print(" [.] Got %r" % response)

    return response