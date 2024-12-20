
import schedule
import time
from bing import bot

call_me=lambda:None
schedule.every().day.do(bot)

while True:
    schedule.run_pending()
    time.sleep(3600)