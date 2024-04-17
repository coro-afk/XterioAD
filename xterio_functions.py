from web3 import Web3,Account
import time
import random
import requests
from fake_useragent import UserAgent
from config import vote_abi
from eth_account.messages import encode_defunct


def current_time():
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")[:-3]
    return cur_time

class Xterio:
    def __init__(self,private_key,code,proxy = None):
        self.private_key = private_key
        self.code = code
        self.proxy = proxy
        self.account = Account.from_key(private_key)
        self.UserAgent = UserAgent().random
        headers = {
            'User-Agent': self.UserAgent,
            "Referer": "https://xter.io",
            "Origin": "https://xter.io/",
            "Sensorsdatajssdkcross": "%7B%22distinct_id%22%3A%2218e9e863069113e-06deb59f7fe507c-3b435c3b-2073600-18e9e86306a18ba%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlOWU4NjMwNjkxMTNlLTA2ZGViNTlmN2ZlNTA3Yy0zYjQzNWMzYi0yMDczNjAwLTE4ZTllODYzMDZhMThiYSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218e9e863069113e-06deb59f7fe507c-3b435c3b-2073600-18e9e86306a18ba%22%7D",
            # 'Authorization':'eyJraWQiOiJYZ0VicUFNaTJrR2Q1Ukg4NXNkUUNXNGNDTExiQ3pmVWxmOVVcL1FqTnNSZz0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiYmM1Y2FjMzItODMyOS00YTY1LWJhMDEtODEzYzVhOTU0Y2RjIiwic3ViIjoiMDQ0MjgwZmYtMDk0My00NDhlLTk0MTYtYzg4ZDhmYjI0MjUyIiwiYXVkIjoiNHAzMHVoaWdrbjBrcWxvMWdoYTl2MnV1OWoiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MTIwNzQ0MDksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5ldS1jZW50cmFsLTEuYW1hem9uYXdzLmNvbVwvZXUtY2VudHJhbC0xX1llSjZPNU41SCIsImNvZ25pdG86dXNlcm5hbWUiOiIwNDQyODBmZi0wOTQzLTQ0OGUtOTQxNi1jODhkOGZiMjQyNTIiLCJleHAiOjE3MTIxNjA4MDksImlhdCI6MTcxMjA3NDQwOSwianRpIjoiZDVhZDM1ODktZDhlYy00Y2U4LWFlNTAtNDE5YTg0ZGIxM2I1In0.mr3l0O9_qrmGM-o2HAMmxhoIUr4lQViJ97KQmIMcugJ5uV1UzOm6zNaRQo0tesKBV61ZmHhlzlMSiiER97lYAG7cAVfsNsVaPtBKwkEmHsOkYIJlqpEJ6gWfuoUpVSRQUhCivSW4qoupmreLPlZo9Ef4ZHolQFw6dAgvXsEgjyi2UY6wUTABcO5UCG2vSx4-_P5KqTfJFaWnTEPg6iItMss7g7cPWbNi_NW3vvHteeEx9ZrsXoBQs5yXldkceRNXEHnRfUsuRdfdsGazg3yp1krDpAMnkAmirIWvg49Kjn-fyo480OtXXEjhAZPX-e5vajFGtf47PuIdYAwckyKf3w'
        }
        self.session = requests.Session()
        self.session.headers = headers

        if proxy is None:
            self.web3 = Web3(Web3.HTTPProvider("https://xterio.alt.technology"))
        else:
            test = proxy
            ip = test.split(":")[0]
            port = int(test.split(":")[1])
            username = test.split(":")[2]
            pwd = test.split(":")[3]
            proxies = {'http': f'http://{username}:{pwd}@{ip}:{int(port)}',
                       'https': f'http://{username}:{pwd}@{ip}:{int(port)}'}
            request_kwargs = {"proxies":{'http': f'http://{username}:{pwd}@{ip}:{int(port)}',
                       'https': f'http://{username}:{pwd}@{ip}:{int(port)}'}
            }
            self.web3 = Web3(Web3.HTTPProvider("https://xterio.alt.technology",request_kwargs=request_kwargs))
            self.session.proxies = proxies

    def bridge(self):
        web3 = Web3(Web3.HTTPProvider("https://bsc-pokt.nodies.app"))
        account = Account.from_key(self.private_key)
        amount = round(random.uniform(0.003, 0.004), 4)
        tx = {
            "from": account.address,
            "to": web3.to_checksum_address("0xc3671e7e875395314bbad175b2b7f0ef75da5339"),
            "value": web3.to_wei(amount, "ether"),
            "nonce": web3.eth.get_transaction_count(account.address),
            "gasPrice": web3.eth.gas_price,
            "chainId": 56,
            "data": "0xb1a1a8820000000000000000000000000000000000000000000000000000000000030d4000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000000"
        }
        tx["gas"] = 743074
        signed_txn = web3.eth.account.sign_transaction(tx, self.private_key)
        transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
        receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
        print(f"{current_time()} | Waiting for Bridge TX to complete...")
        if receipt.status != 1:
            print(f"{current_time()} | Transaction {transaction_hash} failed!")
            time.sleep(random.randint(2, 4))

        print(f"{current_time()} | Bridge hash: {transaction_hash}")
        time.sleep(random.randint(2, 4))

    def get_nonce(self):
        try:
            url = f'https://api.xter.io/account/v1/login/wallet/{self.account.address}'
            res = self.session.get(url)
            if 'err_code' in res.text and res.json()['data']:
                message = res.json()['data']['message']
                signature = self.account.sign_message(encode_defunct(text=message))
                return signature.signature.hex()

            print(f'[{self.account.address}] 获取nonce失败：{res.text}')
            return None
        except Exception as e:
            print(f'[{self.account.address}] 获取nonce异常：{e}')
            return None

    def signin(self):
        print(f"{current_time()} | Starting login in...")
        try:
            signature = self.get_nonce()
            if signature is None:
                return False
            json_data = {
                "address": self.account.address,
                "sign": signature,
                "provider": 'METAMASK',
                'invite_code': '',
                'type': 'eth'
            }
            url = 'https://api.xter.io/account/v1/login/wallet'
            res = self.session.post(url, json=json_data)
            if 'err_code' in res.text and res.json()['data']:
                id_token = res.json()['data']['id_token']
                self.session.headers.update({"Authorization": id_token})

            print(f'[{self.account.address}] 登录成功：{res.text}')
            return False
        except Exception as e:
            print(f'[{self.account.address}] 登录异常：{e}')
            return False

    def submit_code(self):
        count = 0
        print(f'开始邀请码填写---{self.account.address}----{self.code}')
        try:
            url = f'https://api.xter.io/palio/v1/user/{self.account.address}/invite/apply'
            time.sleep(1)
            json_data = {
                'code': self.code
            }
            res = self.session.post(url, json=json_data)
            if 'err_code' in res.text and res.json()['err_code'] == 0:
                print(f'邀请码填写正确---{self.account.address}----{self.code}')
                count += 1
                return count
            else:
                return 0
        except Exception as e:
            print(f'[{self.account.address}] 提交邀请码异常：{e}')


    def claimUtility(self, index):
        print(f"{current_time()} | Starting Claim Utility...")
        try:
            account = Account.from_key(self.private_key)
            data = f"0x8e6e1450000000000000000000000000000000000000000000000000000000000000000{index}"
            tx = {
                "from": account.address,
                "to": self.web3.to_checksum_address("0xBeEDBF1d1908174b4Fc4157aCb128dA4FFa80942"),
                "value": 0,
                "nonce": self.web3.eth.get_transaction_count(account.address),
                "gasPrice": self.web3.eth.gas_price + 20000,
                "chainId": 112358,
                "data": data
            }
            tx["gas"] = int(self.web3.eth.estimate_gas(tx))
            signed_txn = self.web3.eth.account.sign_transaction(tx, self.private_key)
            transaction_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

            print(f"{current_time()} | Waiting for ClaimUtility TX to complete...")
            receipt = self.web3.eth.wait_for_transaction_receipt(transaction_hash)
            if receipt.status != 1:
                print(f"{current_time()} | Transaction {transaction_hash} failed!")
                time.sleep(random.randint(2, 4))
            print(f"{current_time()} | ClaimUtility hash: {transaction_hash}")
            time.sleep(random.randint(2, 4))

            return transaction_hash
        except Exception as e:
            print(f'[{self.account.address}] ClaimUtility 异常：{e}')


    def claimEgg(self):
        print(f"{current_time()} | Starting Claim Egg...")
        try:
            account = Account.from_key(self.private_key)
            tx = {
                "from": account.address,
                "to": self.web3.to_checksum_address("0xBeEDBF1d1908174b4Fc4157aCb128dA4FFa80942"),
                "value": 0,
                "nonce": self.web3.eth.get_transaction_count(account.address),
                "gasPrice": self.web3.eth.gas_price + 20000,
                "chainId": 112358,
                "data": "0x48f206fc"
            }
            tx["gas"] = int(self.web3.eth.estimate_gas(tx))
            signed_txn = self.web3.eth.account.sign_transaction(tx, self.private_key)
            transaction_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
            print(f"{current_time()} | Waiting for ClaimEgg TX to complete...")
            receipt = self.web3.eth.wait_for_transaction_receipt(transaction_hash)
            if receipt.status != 1:
                print(f"{current_time()} | Transaction {transaction_hash} failed!")
                time.sleep(random.randint(2, 4))
            print(f"{current_time()} | ClaimEgg hash: {transaction_hash}")
            time.sleep(random.randint(2, 4))
        except Exception as e:
            print(f'[{self.account.address}] claimEgg 异常：{e}')


    def claimChatNft(self):
        print(f"{current_time()} | Starting Claim ChatNft...")
        try:
            account = Account.from_key(self.private_key)
            tx = {
                "from": account.address,
                "to": self.web3.to_checksum_address("0xBeEDBF1d1908174b4Fc4157aCb128dA4FFa80942"),
                "value": 0,
                "nonce": self.web3.eth.get_transaction_count(account.address),
                "gasPrice": self.web3.eth.gas_price + 20000,
                "chainId": 112358,
                "data": "0x8cb68a65"
            }
            tx["gas"] = int(self.web3.eth.estimate_gas(tx))
            signed_txn = self.web3.eth.account.sign_transaction(tx, self.private_key)
            transaction_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
            print(f"{current_time()} | Waiting for claimChatNft TX to complete...")
            receipt = self.web3.eth.wait_for_transaction_receipt(transaction_hash)
            if receipt.status != 1:
                print(f"{current_time()} | Transaction {transaction_hash} failed!")
                time.sleep(random.randint(2, 4))
            print(f"{current_time()} | claimChatNft hash: {transaction_hash}")
            time.sleep(random.randint(2, 4))
            return transaction_hash
        except Exception as e:
            print(f'[{self.account.address}] claimChatNft 异常：{e}')


    def chat(self):
        print(f"{current_time()} | Starting Chat...")
        url = f"https://3656kxpioifv7aumlcwe6zcqaa0eeiab.lambda-url.eu-central-1.on.aws/?address={self.account.address}"
        data_json = {
            'answer': "In a small town draped in twilight, Ivy, a painter, and Rowan, a musician, found solace under the old oak tree. With every brushstroke, Ivy captured the melodies Rowan played, their art intertwining like vines. As seasons changed, so did their affection, growing deeper with each note and hue. Beneat"
        }
        res = self.session.post(url, data=data_json)
        txHash = self.claimChatNft()
        try:
            url = 'https://api.xter.io/baas/v1/event/trigger'
            json_data = {
                'eventType': 'PalioIncubator::*',
                'network': 'XTERIO',
                'txHash': txHash
            }
            res = self.session.post(url, json=json_data)
            print(res.json())
            if 'err_code' in res.text and res.json()['err_code'] == 0:
                print(f'chatNFT领取完成')
            time.sleep(random.randint(1, 5))
        except Exception as e:
            print(f'[{self.account.address}] chatNFT异常：{e}')
            return False

    def trigger(self):
        print(f"{current_time()} | Starting trigger...")
        try:
            tasks = [1, 2, 3]
            random.shuffle(tasks)
            for i in tasks:
                txHash = self.claimUtility(i)
                url = 'https://api.xter.io/baas/v1/event/trigger'
                json_data = {
                    'eventType': 'PalioIncubator::*',
                    'network': 'XTERIO',
                    'txHash': txHash
                }
                res = self.session.post(url, json=json_data)
                if 'err_code' in res.text and res.json()['err_code'] == 0:
                    print(f'第{i}个小人物完成')
                time.sleep(random.randint(1, 5))
            # logging.error(f'[{self.account.address}] 3个小人物成功')
            return True
        except Exception as e:
            print(f'[{self.account.address}] 3个小任务异常：{e}')
            return False

    def prop(self):
        print(f"{current_time()} | Starting prop...")
        try:
            url = f'https://api.xter.io/palio/v1/user/{self.account.address}/prop'
            count = 0
            for i in range(1, 4):
                data_json = {
                    'prop_id': i
                }
                res = self.session.post(url, json=data_json)
                count += 1
                time.sleep(random.randint(0,2))
            print(f'prod成功了{count}个')
        except Exception as e:
            print(f'[{self.account.address}] prop异常：{e}')
            return False

    def vote(self):
        print(f"{current_time()} | Starting vote...")
        account = Account.from_key(self.private_key)
        addr = account.address
        # 获取总票数
        url_getTickets = f"https://api.xter.io/palio/v1/user/{addr}/ticket"
        res_getTickets = self.session.get(url_getTickets)
        res = res_getTickets.json()
        total = res["data"]["total_ticket"]
        # 获取已投票数量
        contract = self.web3.eth.contract(
            address=self.web3.to_checksum_address("0x73e987FB9F0b1c10db7D57b913dAa7F2Dc12b4f5"),
            abi=vote_abi,
        )
        voted = contract.functions.userVotedAmt(account.address).call()

        # 获取投票合约入参
        vote_num = total - voted
        url = f"https://api.xter.io/palio/v1/user/{addr}/vote"
        data = {
            "index": 0,
            "num": vote_num
        }
        response = self.session.post(url, data)
        if response.status_code == 200:
            response = response.json()
        sign = response["data"]["sign"]
        index = response["data"]["index"]
        num = response["data"]["num"]
        total_num = response["data"]["total_num"]
        expire_time = response["data"]["expire_time"]
        contract_addr = response["data"]["voter_address"]


        tx = contract.functions.vote(index, num, total_num, expire_time, sign).build_transaction(
            {
                "from": account.address,
                "value": 0,
                "nonce": self.web3.eth.get_transaction_count(account.address),
                "gasPrice": self.web3.eth.gas_price + 20000,
                "chainId": 112358,
            }
        )
        tx["gas"] = int(self.web3.eth.estimate_gas(tx))
        signed_txn = self.web3.eth.account.sign_transaction(tx, self.private_key)
        transaction_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
        print(f"| Waiting for Vote TX to complete...")
        receipt = self.web3.eth.wait_for_transaction_receipt(transaction_hash)
        if receipt.status != 1:
            print(f"| Transaction {transaction_hash} failed!")
            time.sleep(random.randint(2, 4))
        print(f"{current_time()} | Vote hash: {transaction_hash}")
        time.sleep(random.randint(2, 4))

    def task_x(self):
        print(f"{current_time()} | Starting Go task in twitter...")
        account = Account.from_key(self.private_key)
        try:
            task_id = [11, 17, 15, 18, 12, 13, 14]
            random.shuffle(task_id)
            for task in task_id:
                url = f"https://api.xter.io/palio/v1/user/{account.address}/task/report"
                data = {
                    "task_id" : task
                }
                response = self.session.post(url,data)
                res = response.json()
                if res["err_code"] == 0:
                    print(f"{current_time()} | {task} Go success")
                else:
                    print(f"{current_time()} | {task} Go fail")
                time.sleep(2)
                url = f"https://api.xter.io/palio/v1/user/{account.address}/task"
                data = {
                    "task_id": task
                }
                response = self.session.post(url, data)
                res = response.json()
                if res["err_code"] == 0:
                    print(f"{current_time()} | {task} Claim success")
                else:
                    print(f"{current_time()} | {task} Claim fail")
                time.sleep(2)


        except Exception as e:
            print(f'[{self.account.address}] Go task 异常：{e}')


    def get_info(self):
        try:
            if 'Authorization' not in self.session.headers:
                self.signin()
            self.claimEgg()
            self.submit_code()
            self.chat()
            self.trigger()
            self.prop()
            self.task_x()
            self.task_x()
            self.vote()

        except Exception as e:
            print(f'[{self.account.address}] 获取信息异常：{e}')

    def invite(self):
        try:
            if 'Authorization' not in self.session.headers:
                self.signin()
            self.claimEgg()
            count = self.submit_code()
            return count

        except Exception as e:
            print(f'[{self.account.address}] 获取信息异常：{e}')

    def daily(self):
        try:
            if 'Authorization' not in self.session.headers:
                self.signin()
            self.trigger()
            self.prop()
            self.task_x()

        except Exception as e:
            print(f'[{self.account.address}] 获取信息异常：{e}')


if __name__ == '__main__':
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
        DY = Xterio(keys[i], codes[0],proxys[i])
        # 私钥
        DY.get_info()
        count += 1
        time.sleep(2)