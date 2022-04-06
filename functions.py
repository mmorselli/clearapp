from config import INDEXER_CLIENT,ALGOD_CLIENT,ACCOUNT_PRIVATE_KEY
from algosdk import future

################################################
def app_clear_state(account_public_key,appid):

    params = ALGOD_CLIENT.suggested_params()

    unsigned_tx = future.transaction.ApplicationClearStateTxn(account_public_key, params, appid)
    signed_tx = unsigned_tx.sign(ACCOUNT_PRIVATE_KEY)

    txid = ALGOD_CLIENT.send_transaction(signed_tx)

    # wait for confirmation 
    try:
        future.transaction.wait_for_confirmation(ALGOD_CLIENT, txid, 4)
        ALGOD_CLIENT.pending_transaction_info(txid)
        #print("Cleared app-id: ",transaction_response['txn']['txn']['apid'])
        return True
    except Exception as err:
        print("\nError: ",err,"\n")
        return False

################################################
def get_apps_list(account_public_key):
    response = INDEXER_CLIENT.account_info(account_public_key)

    if not 'apps-local-state' in response['account']:
        return False

    applist = {}
    count = 0;
    for app in response['account']['apps-local-state']:
        if(app['deleted']==False):
            count = count + 1
            applist[count] = app['id']

    if (count > 0):
        return applist
    else:
        return False

################################################
def app_menu(account_public_key):

    

    print(f"\n{account_public_key} applications\n")

    choice=True
    while choice:
        applist = get_apps_list(account_public_key)
        
        if not applist:
            return False
        
        for appid in applist:
            print(f"{appid}. {applist[appid]}")
        
        print("0. EXIT")
        
        choice=input(f"\nWhat app do you want to clear? [0-{len(applist)}]")
        ichoice=int(choice)
        if ichoice in range(1,len(applist)+1):
            result = app_clear_state(account_public_key,applist[ichoice])
            if result:
                print(f"\nApp ID {applist[ichoice]} cleared\n")
        elif ichoice==0: 
            #choice = None
            return True
        else:
            print("\nNot Valid Choice Try again\n")