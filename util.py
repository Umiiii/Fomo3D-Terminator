import time
from threading import Thread

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def log(s):
    print("[",timestamp_datetime(time.time()),"]",s)


