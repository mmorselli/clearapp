from algosdk.v2client import algod, indexer
from algosdk import mnemonic


##################################################################
# config

NETWORK = 'testnet' # select testnet o mainnet
API_KEY = "" # purestake (free) key
MNEMONIC_PHRASE = "" # 25 word PK, without comma

# end config
##################################################################

ALGOD_ADDRESS = 'https://'+NETWORK+'-algorand.api.purestake.io/ps2' # algod client: select testnet or mainnet
INDEXER_ADDRESS = 'https://'+NETWORK+'-algorand.api.purestake.io/idx2' # indexer client: select testnet or mainnet

ALGOD_TOKEN = API_KEY
HEADERS = {"X-API-Key": API_KEY}
ALGOD_CLIENT = algod.AlgodClient(ALGOD_TOKEN,ALGOD_ADDRESS,HEADERS)
INDEXER_CLIENT = indexer.IndexerClient(ALGOD_TOKEN, INDEXER_ADDRESS, HEADERS)

ACCOUNT_PRIVATE_KEY = mnemonic.to_private_key(MNEMONIC_PHRASE)
ACCOUNT_PUBLIC_KEY = mnemonic.to_public_key(MNEMONIC_PHRASE)