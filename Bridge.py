import random
import time
from xterio_functions import Xterio


keys = []
with open('error.txt', 'r') as file:
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
with open('error_ip.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        proxy = line.strip()
        proxys.append(proxy)

for i in range(0, len(keys)):
    DY = Xterio(keys[i], codes[0], proxys[i])
    DY.bridge()
    print(f"已处理{i+1}个钱包")
