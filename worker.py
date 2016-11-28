import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('redis://redistogo:897d4c29fb07e5d500bb38d2c26c64f1@crestfish.redi stogo.com:9158/')

conn = redis.from_url(redis_url)


def get_conn():
    return conn


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
