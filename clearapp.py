from config import ACCOUNT_PUBLIC_KEY
from functions import app_menu

result = app_menu(ACCOUNT_PUBLIC_KEY)

if(result):
    print("\nGoodbye\n")
else:
    print("\nNo apps found\n")