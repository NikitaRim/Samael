import time
import struct
import random
import hashlib

import datetime
from multiprocessing import Process

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

voodoo_magic = {}
totalsum = 0

def voodoo(first_number, how_many):
    num = first_number
    for i in range(how_many):
        voodoo_magic[num] = slow_calculate(num)
        num+=1
"""
if __name__ == "__main__":
    now = datetime.datetime.now()
    Process = []
    for i in range(50):
        Process.append(Process(target = voodoo, args=(i*10,10)))
        Process[i].start()
    for i in range(50):
        Process[i].join()
    runtime = datetime.datetime.now() - now
"""
print(slow_calculate(5))
