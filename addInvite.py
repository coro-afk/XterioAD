import random
import time
import multiprocessing
from web3 import Web3,Account
from xterio_functions import Xterio

addCount = 0
for i in range(1, 3):
    account = Account.create()

    print(account.key.hex())
    gate_private = "e0dcdb098d8c28c8dd6ab0dda0910fc5a9b1d06e274fe33a3078dce227a30ebe"
    gate = Account.from_key(gate_private)
    proxy = "45.249.106.90:5787:taqomegr:PTHY0326"
    request_kwargs = {"proxies": {'http': f'http://taqomegr:PTHY0326@45.249.106.90:5787',
                                  'https': f'http://taqomegr:PTHY0326@45.249.106.90:5787'}
                      }
    web3 = Web3(Web3.HTTPProvider("https://xterio.alt.technology"))
    tx = {
        "from": gate.address,
        "to": account.address,
        "value": web3.to_wei(0.000001, "ether"),
        "nonce": web3.eth.get_transaction_count(gate.address),
        "gasPrice": web3.eth.gas_price + 300000,
        "chainId": 112358,
    }
    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_txn = web3.eth.account.sign_transaction(tx, gate_private)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

    print(f"| Waiting for BNB transfer TX to complete...")
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        print(f"| Transaction {transaction_hash} failed!")
    print(f"| BNB transfer hash: {transaction_hash}")
    xterio = Xterio(account.key.hex(), "ece4e9090d07f755770b35e5ffe1e570")

    count = xterio.invite()
    if count is not None:
        addCount = addCount + count
    else:
        # 此次失败 则将其私钥记录入文本中
        with open("./fail_private.txt", "a") as f:
            f.write(account.key.hex() + "\n")
    time.sleep(random.randint(3, 5))
    print(f"*****************************已完成{addCount}个****************************")

# proxy = "45.249.106.90:5787:taqomegr:PTHY0326"
# keys = []
# with open('fail_private.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         key = line.strip()
#         keys.append(key)
# for key in keys:
#     xterio = Xterio(key,
#                     "c0f667924357478f8845fbf3fad45a90", proxy)
#     xterio.invite()

