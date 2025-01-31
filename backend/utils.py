import random
from fake_useragent import UserAgent
import socks
import socket
import os

def enable_tor_proxy():
    """ Route traffic via Tor (tor-proxy container). """
    socks.set_default_proxy(socks.SOCKS5, 'tor-proxy', 9050)
    socket.socket = socks.socksocket

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def random_sleep(low=5, high=15):
    """ Sleep a random interval between low and high seconds. """
    import time
    delay = random.randint(low, high)
    time.sleep(delay)
