from algosdk.v2client import algod, indexer
from algosdk import mnemonic


##################################################################
# config

NETWORK = 'testnet' # select testnet o mainnet
MNEMONIC_PHRASE = "" # 25 word PK, without comma - if the account is rekeyed the mnemonic must be that of the rekeyed account
ACCOUNT_PUBLIC_KEY = ""

# end config
##################################################################

if not MNEMONIC_PHRASE:
    print("\nPlease open config.py and fill the config section\n")
    quit()

ALGOD_ADDRESS = 'https://'+NETWORK+'-api.algonode.cloud'
INDEXER_ADDRESS = 'https://'+NETWORK+'-idx.algonode.cloud'

ALGOD_TOKEN = ""
ALGOD_CLIENT = algod.AlgodClient(ALGOD_TOKEN,ALGOD_ADDRESS)
INDEXER_CLIENT = indexer.IndexerClient(ALGOD_TOKEN, INDEXER_ADDRESS)

ACCOUNT_PRIVATE_KEY = mnemonic.to_private_key(MNEMONIC_PHRASE)
