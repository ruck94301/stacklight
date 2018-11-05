import logging
import socket
import time


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

HOST = '10.0.0.7'
PORT = 135
address = (HOST, PORT)


class Lamp:
    basis = ['W'] + [0, 0] + [100] * 5
    def __init__(self, index):
        self.index = index
    
    def on(self):
        command = ''.join(basis[:3+index] + [1] + basis[3+index:])
        logger.debug('command: %r' % command)
        # s.send(command)


class Stacklight:
    def __init__():
        s = socket.connect(address)

    red = Lamp(1)
    amber = Lamp(2)
    green = Lamp(3)
    white = Lamp(4)  # aka "clear"
    blue = Lamp(5)


if __name__ == '__main__':
    stacklight = Stacklight()
    
    stacklight.off()
    stacklight.red.on()
    time.sleep(0.500)
    stacklight.red.off()
