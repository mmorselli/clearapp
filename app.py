from algosdk.v2client import algod
from algosdk import mnemonic,future

##################################################################
# config
API_KEY = "" # purestake (free) key
ALGOD_ADDRESS = 'https://testnet-algorand.api.purestake.io/ps2' # select testnet or mainnet
MNEMONIC_PHRASE = "..." # 25 word PK, without comma
APP_INDEX = 62368684 # application ID to clear
##################################################################

ALGOD_TOKEN = API_KEY
HEADERS = {"X-API-Key": API_KEY}
ALGOD_CLIENT = algod.AlgodClient(ALGOD_TOKEN,ALGOD_ADDRESS,HEADERS)

account_private_key = mnemonic.to_private_key(MNEMONIC_PHRASE)
account_public_key = mnemonic.to_public_key(MNEMONIC_PHRASE)

params = ALGOD_CLIENT.suggested_params()

unsigned_tx = future.transaction.ApplicationClearStateTxn(account_public_key, params, APP_INDEX)
signed_tx = unsigned_tx.sign(account_private_key)

txid = ALGOD_CLIENT.send_transaction(signed_tx)

# wait for confirmation 
try:
    confirmed_txn = future.transaction.wait_for_confirmation(ALGOD_CLIENT, txid, 4)
    # display results
    transaction_response = ALGOD_CLIENT.pending_transaction_info(txid)
    print("Cleared app-id: ",transaction_response['txn']['txn']['apid']) 
except Exception as err:
    print("Error: ",err)

