import requests
from time import sleep
import random


class RequestsPlus:

    def __init__(self, max_retries=10, header=None):
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
        self.session.mount('https://', adapter)
        self.header = header

    def get(self, url, timeout=60, p_sleep=0, sleep_time_mutiplier=10):
        prob = random.random()
        if prob < p_sleep:
            sleep(sleep_time_mutiplier * (1 - prob))
        return self.session.get(url, headers=self.header, timeout=timeout)
