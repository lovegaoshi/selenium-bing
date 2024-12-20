import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from search_query import search_query
from discord import send_discord_message, alert_discord_message

def init():
    options = Options()
    #options.add_argument(f"--profile-directory=Profile 1")
    options.add_argument(r"user-data-dir=/home/seluser/.config/google-chrome-unstable")
    driver = webdriver.Remote(command_executor='http://selenium:4444', options=options)
    return driver

def search(driver):
    driver.get('https://www.bing.com/search?pglt=297&q=google')
    time.sleep(3)
    for i in range(35):
        searchq = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        searchq.clear()
        searchq.send_keys(random.choice(search_query), Keys.RETURN)
        time.sleep(random.uniform(5, 10))

def daily(driver):
    driver.get('https://rewards.bing.com/')
    time.sleep(30)
    for i in range(1, 4):
        daily_set_element = driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{i}]/div/card-content/mee-rewards-daily-set-item-content')
        daily_set_element.click()
        time.sleep(random.uniform(5, 10))

def alert_daily_reward(driver):
    try:    
        driver.get('https://rewards.bing.com/')
        points = driver.find_element(By.XPATH, '//*[@id="dailypointToolTipDiv"]/p').text
        msg = f'[bing] rewards bot has netted {points} points for you today <3'
        send_discord_message(msg)
        points = driver.find_element(By.XPATH, '//*[@id="balanceToolTipDiv"]/p').text
        msg = f'[bing] now you have {points} points total.'
        send_discord_message(msg)
        
    except:
        alert_discord_message('[bing] rewards bot failed! HELP!')

def bot():
    try:
        driver = init()
        search(driver)
        daily(driver)
        alert_daily_reward(driver)
        driver.close()
    except:
        alert_discord_message('[bing] rewards bot failed! HELP!')

if __name__ == "__main__":
    bot()
