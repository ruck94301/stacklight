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

red_on = '5700016464646464'.decode('hex')
red_off = '5700006464646464'.decode('hex')


def send(payload):
    'send payload to new socket, read response, & close socket'
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

    logger.debug('payload: %r' % payload)
    result = s.send(payload)
    logger.debug('send() result: %r' % result)
    result = s.recv(4096)
    logger.debug('recv() result: %r' % result)

    # s.shutdown(socket.SHUT_RDWR)
    s.close()
    return result


result = send(red_on)

time.sleep(10)

result = send(red_off)

time.sleep(10)

logger.debug('exiting...')
