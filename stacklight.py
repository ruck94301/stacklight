import logging
import socket
import struct
import time


logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

HOST = '10.0.0.7'
PORT = 135
address = (HOST, PORT)

lamp_index = {
    'red': 0, 
    'yellow': 1, 
    'green': 2,
    'blue': 3,
    'white': 4,
    }

red_on = '5700016464646464'.decode('hex')
red_off = '5700006464646464'.decode('hex')


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Windows uses shorts instead of ints in struct linger, hence format
    # 'hh' instead of 'ii' for the pair.
    s.setsockopt(
        socket.SOL_SOCKET,  # level
        socket.SO_LINGER,  # optname
        struct.pack('hh', 1, 0),  # value
        )
    s.connect(address)
    logger.debug('s: %r' % s)
    return s

def send(payload):
    'send payload to new socket, read response, & close socket'
    s = connect()

    logger.debug('payload: %r' % payload)
    result = s.send(payload)
    logger.debug('send() result: %r' % result)
    result = s.recv(4096)
    logger.debug('recv() result: %r' % result)

    # s.shutdown(socket.SHUT_RDWR)
    s.close()
    return result



# neutral command
basis = ''.join(
    ['W'] + [b.decode('hex') for b in ['00'] + ['64']*5 + ['64']]
    )
    
# stacklight off
command = ''.join(
    ['W'] + [b.decode('hex') for b in ['00'] + ['00']*5 + ['00']]
    )
result = send(command)

# stacklight red on
i = lamp_index['red']
command = basis[:2+i] + '01'.decode('hex') + basis[2+i+1:]
result = send(command)

time.sleep(10)

# stacklight red off
i = lamp_index['red']
command = basis[:2+i] + '00'.decode('hex') + basis[2+i+1:]
result = send(command)

time.sleep(10)

logger.debug('exiting...')
