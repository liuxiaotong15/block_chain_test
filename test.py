from web3.auto.infura import w3
from web3 import Web3
import web3

addr = '0x05FAa9F14973c850A7070A1FFFeD601B0ae0a739' # contract address
ABI = ''

with open('./abi') as fd:
    ABI = fd.read()
print(ABI)

# from eth_account import Account
# p_key = 0xfaaaaaaaaaa # secret, private key of metamask
# acct = Account.from_key(p_key)
# print(acct.address)

contract = w3.eth.contract(addr, abi=ABI)
print(contract.address)

# user = '0xb2f133052129637450a8518d26be81040d307e07'
# user = '0xb9266c210b0b585c1f879b5df0b5b2f2f6eb144b'
# user = '0x92f71B1a1161e88588b16363b3bC242aF14ED95d' # xuzhe
# user = '0x8fbe099a92a2b1ab95fdb644ae1afa3027af71e1'
user = '0x879e932b55c14Ab7CEEBb74FE94D2015FDC785B2' # xiaotong
# -------------------------read --------------------

print(contract.caller.CheckCount(Web3.toChecksumAddress(user)))
cnt = contract.caller.CheckCount(Web3.toChecksumAddress(user))

print(contract.caller.RecordsCount)

for i in range(cnt):
    print(contract.caller.Check(Web3.toChecksumAddress(user), i))


# # -------------------- write ----------------------
# # not infuta
# # contract.functions.Say('Buy ETH, sell BTC, please,')
# 
# # infura
# trans = contract.functions.Say('Buy ETH, sell BTC, please,').buildTransaction({'nonce': w3.eth.getTransactionCount(Web3.toChecksumAddress(acct.address))})
# print(trans)
# 
# # signed_trans = acct.sign_transaction(trans, private_key=p_key)
# signed_trans = acct.sign_transaction(trans)
# print(signed_trans.hash, signed_trans.rawTransaction)
# 
# ret = w3.eth.sendRawTransaction(signed_trans.rawTransaction)
# print(ret)
