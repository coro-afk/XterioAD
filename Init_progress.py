import random
import time
from xterio_functions import Xterio
import numpy as np

keys = []
with open('keys.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        key = line.strip()
        keys.append(key)

codes = []
with open('invite.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        code = line.strip()
        codes.append(code)

proxys = []
with open('proxy.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        proxy = line.strip()
        proxys.append(proxy)

arr = np.arange(1, len(keys))
np.random.shuffle(arr)
count = 0
for i in arr:
    DY = Xterio(keys[i], codes[0], proxys[i])
    DY.get_info()
    count = count + 1
    time.sleep(random.randint(1,3))
    print(f"已处理{count}个号")