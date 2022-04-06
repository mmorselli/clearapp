from config import ACCOUNT_PUBLIC_KEY
from functions import app_menu


# ACCOUNT_PUBLIC_KEY = "TTBHGWQJT35QT4F4DGI6M63LSCP4SXAJJ3LZZ4GINXHGTGUPNEPKAHIRII"

result = app_menu(ACCOUNT_PUBLIC_KEY)

if(result):
    print("\nGoodbye\n")
else:
    print("\nNo apps found\n")