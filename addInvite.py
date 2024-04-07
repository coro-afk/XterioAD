import random
import time
import multiprocessing
from web3 import Web3,Account
from xterio_functions import Xterio


web3 = Web3(Web3.HTTPProvider("https://xterio.alt.technology"))
nonce = web3.eth.get_transaction_count("0x907d281c54667E4aae39e1FA1Ca00ADDC8529739")
# code 代表邀请码
codes = []
with (open('code_keys.txt', 'r') as file):
    lines = file.readlines()
    for line in lines:
        code = line.strip()
        codes.append(code)

for code in codes:
    addCount = 0
    for i in range(1, 9999):
        if addCount < 10:
            account = Account.create()
            private_key = account.key.hex()
            print(account.key.hex())
            gate_private = "e0dcdb098d8c28c8dd6ab0dda0910fc5a9b1d06e274fe33a3078dce227a30ebe"
            gate = Account.from_key(gate_private)
            proxy = "45.249.106.90:5787:taqomegr:PTHY0326"
            # # request_kwargs = {"proxies": {'http': f'http://taqomegr:PTHY0326@45.249.106.90:5787',
            #                               'https': f'http://taqomegr:PTHY0326@45.249.106.90:5787'}
            #                   }
            web3 = Web3(Web3.HTTPProvider("https://xterio.alt.technology"))
            # print(web3.is_connected())
            tx = {
                "from": gate.address,
                "to": account.address,
                "value": web3.to_wei(0.000006, "ether"),
                "nonce": nonce,
                "gasPrice": web3.eth.gas_price,
                "chainId": 112358,
            }
            tx["gas"] = int(web3.eth.estimate_gas(tx))
            gasprice, gas = tx["gasPrice"], tx["gas"]
            signed_txn = web3.eth.account.sign_transaction(tx, gate_private)
            transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

            print(f"| Waiting for BNB transfer TX to complete...")
            receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
            if receipt.status != 1:
                print(f"| Transaction {transaction_hash} failed!")
            print(f"| BNB transfer hash: {transaction_hash}")

            nonce = nonce + 1

            xterio = Xterio(account.key.hex(), code)
            xterio.signin()
            # 复写claimEgg函数
            print(f"| Starting Claim Egg...")
            try:
                account = Account.from_key(private_key)
                tx = {
                    "from": account.address,
                    "to": web3.to_checksum_address("0xBeEDBF1d1908174b4Fc4157aCb128dA4FFa80942"),
                    "value": 0,
                    "nonce": web3.eth.get_transaction_count(account.address),
                    "gasPrice": gasprice,
                    "gas": 150000,
                    "chainId": 112358,
                    "data": "0x48f206fc"
                }
                # tx["gas"] = int(self.web3.eth.estimate_gas(tx))
                signed_txn = web3.eth.account.sign_transaction(tx, private_key)
                transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
                print(f"| Waiting for ClaimEgg TX to complete...")
                receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
                if receipt.status != 1:
                    print(f"| Transaction {transaction_hash} failed!")
                    time.sleep(random.randint(2, 4))
                print(f"| ClaimEgg hash: {transaction_hash}")
                time.sleep(random.randint(2, 4))
            except Exception as e:
                print(f'[{account.address}] claimEgg 异常：{e}')
            # count = xterio.invite()
            count = xterio.submit_code()
            if count != 0:
                addCount = addCount + count
                with open("./succ_private.txt", "a") as f:
                    f.write(account.key.hex() + "\n")
            else:
                # 此次失败 则将其私钥记录入文本中
                with open("./fail_private.txt", "a") as f:
                    f.write(account.key.hex() + "\n")
            time.sleep(random.randint(2, 4))
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
#                    "f3c840a322bb72ddfb679e35010971b0", proxy)
#     xterio.invite()

