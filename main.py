# Import all dependencies
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram_send
from datetime import datetime
import time

anniversaire = 1
day = datetime.now().strftime('%A')
year = datetime.now().strftime('%Y')
date = datetime.now().strftime('%d-%m')
Heure = datetime.now().strftime('%H:%M:%S')
weather = "none"

#print(f"La date est le {date}")
#print(f"L'heure est {Heure}")



while True:

    time.sleep(3)
    
    
    
    if date == '18-08':
        if anniversaire == 0:
            telegram_send.send(messages=[f"Bon anniversaire monsieur pour ce {2022-2000}eme anniversaire"])
            anniversaire = 1
    if date == '19-08':
        anniversaire = 1
#    else:
#        print("Aujourd'hui on est pas le 16 aout")
