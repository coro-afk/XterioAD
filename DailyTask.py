from xterio_functions import Xterio


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

count = 0
for i in range(0, len(keys)):
    DY = Xterio(keys[i], codes[0], proxys[i])
    DY.daily()
