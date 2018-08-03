from config import *
from util import *
import binascii

assert ADDRESS != "0x0000000000000000000000000000000000000000", "Please set your address in config.py first."
assert SECRET != "0000000000000000000000000000000000000000000000000000000000000000", "Please set your private key in config.py first."
assert len(ADDRESS) == 42, "Address length is incorrect, please check again."
assert RPC_ADDRESS !="https://mainnet.infura.io/####################","RPC incorrect"
assert len(SECRET) == 64, "Private key length is incorrect, please check again."
assert len(FOMO3D_ABI) >= 0 , "Contract ABI is incorrect, please check again."
assert len(FOMO3D_CONTRACT_ADDRESS) == 42, "Contract address is incorrect, please check again."
contract = w3.eth.contract(abi=FOMO3D_ABI, address=FOMO3D_CONTRACT_ADDRESS)


# You can customize your functions with abi
# Fomo3d contract functions start
def get_buy_price():
    return contract.functions.getBuyPrice().call()


def get_time_left():
    return contract.functions.getTimeLeft().call()


def get_current_round_info():
    '''
    * @return eth invested during ICO phase
    * @return round id
    * @return total keys for round
    * @return time round ends
    * @return time round started
    * @return current pot
    * @return current team ID & player ID in lead
    * @return current player in leads address
    * @return current player in leads name
    * @return whales eth in for round
    * @return bears eth in for round
    * @return sneks eth in for round
    * @return bulls eth in for round
    * @return airdrop tracker # & airdrop pot
    '''
    return contract.functions.getCurrentRoundInfo().call()


# Fomo3d contract functions end
def get_tx_count():
    return w3.eth.getTransactionCount(ADDRESS)

def get_tx_result(txid):
    if len(txid) != 66:
        return
    start_time = time.time()
    txresult = w3.eth.getTransactionReceipt(txid)
    while txresult == None:
        log("Still waiting for tx "+txid+" to complete.")
        time.sleep(5)
        txresult = w3.eth.getTransactionReceipt(txid)
    #print(txresult)
    cumulative_gas = txresult["gasUsed"]
    result = txresult["status"]
    if result == 0x0:
        result = "Failed"
    else:
        result = "Success"
    log("Purchase key success!")
    log("Used gas: "+str(cumulative_gas))
    log("Used time: "+str(time.time()-start_time))
    log("Status: "+result)
    return


def buy_key():
    '''
    :return: The transaction id
    '''
    tx_count = get_tx_count()
    price = get_buy_price()
    log("Key price : "+str (price / 1e18))
    #price = price * 1.01 # Better to do that if you really want to get the pot
    data = {
        'gas': GAS_LIMIT,
        'gasPrice': w3.toWei(GAS_PRICE, 'gwei'),
        'value': price,
        'nonce': w3.toHex(tx_count)
    }
    tx = contract.functions.buyXname(bytes("","utf-8"),TEAM).buildTransaction(
        data
    )
    #print(tx)
    log("Use gas price "+ str(GAS_PRICE))
    log("Use gas limit "+ str(GAS_LIMIT))
    signed_tx = w3.eth.account.signTransaction(tx, SECRET)
    txid = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    txid = "0x"+str(binascii.hexlify(txid)).replace("b'",'').replace("'","")
    log("txid = "+str(txid))
    return txid


def print_current_info(data):
    keys = str(round(data[2] / 1e18, 3))
    pots = str(round(data[5] / 1e18, 3))
    last_player = data[7]
    last_playername = str(data[8]).replace("b'","").replace("\\x00","").replace("'","")
    log("Keys " + keys)
    log("Pots " + pots + " Ether")
    log("Last key holder: " + last_player + " " + last_playername)