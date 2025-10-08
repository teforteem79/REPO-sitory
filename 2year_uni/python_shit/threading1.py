import threading as th
import time
import logging

def worker():
    print(th.current_thread().name, 'Starting')
    time.sleep(0.2)
    print(th.current_thread().name, 'Exiting')

def my_service():
    print(th.current_thread().name, 'Starting')
    time.sleep(0.3)
    print(th.current_thread().name, 'Exiting')

t = th.Thread(name='my_service', target=my_service)
w = th.Thread(name='worker', target=worker)
w2 = th.Thread(target=worker) # використати ім'я за замовчуванням

# w.start()
# w2.start()
# t.start()


def daemon():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)s) %(message)s', )

d = th.Thread(name='deamon', target=daemon, daemon=True)
t = th.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()