import logging
import socket
import time


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

HOST = '10.0.0.7'
PORT = 135
address = (HOST, PORT)


if __name__ == '__main__':
    # neutral command
    basis = ''.join(['W'] 
        + [b.decode('hex') for b in ['00'] + ['64']*5 + ['64']]
        )
        
    lamp_index = {
        'red': 0, 
        'yellow': 1, 
        'green': 2,
        'blue': 3,
        'white': 4,
        }

    # s = socket.socket()

    # stacklight off
    command = ''.join(['W'] 
        + [b.decode('hex') for b in ['00'] + ['00']*5 + ['00']]
        )
    logger.debug('command: %r' % command)
    # s.send(command)
        
    # stacklight red on
    i = lamp_index['red']
    command = basis[:2+i] + '01'.decode('hex') + basis[2+i+1:]
    logger.debug('command: %r' % command)
    # s.send(command)
    
    time.sleep(0.500)
    
    # stacklight red off
    i = lamp_index['red']
    command = basis[:2+i] + '00'.decode('hex') + basis[2+i+1:]
    logger.debug('command: %r' % command)
    # s.send(command)

    time.sleep(3)
