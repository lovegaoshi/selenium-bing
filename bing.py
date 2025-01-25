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

def search(driver, count = 35, initialize = False):
    if count < 1:
        return driver
    if initialize:
        driver.get('https://www.bing.com/search?pglt=297&q=google')
        time.sleep(60)
    try:
        time.sleep(10)
        searchq = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        searchq.clear()
        searchq.send_keys(random.choice(search_query), Keys.RETURN)
        time.sleep(random.uniform(5, 10))
        return search(driver, count - 1)
    except KeyboardInterrupt:
        return driver
    except Exception:
        alert_discord_message('[bing] failed to init search. waiting 10 minutes.')
        time.sleep(600)
        try:
            driver.quit()
        except:
            pass
        return search(init(), count, True)

def daily(driver):
    driver.get('https://rewards.bing.com/')
    time.sleep(30)
    for i in range(1, 4):
        daily_set_element = driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{i}]/div/card-content/mee-rewards-daily-set-item-content')
        daily_set_element.click()
        time.sleep(random.uniform(5, 10))
    return driver

def alert_daily_reward(driver):
    try:    
        driver.get('https://rewards.bing.com/')    
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(30)
        points = driver.find_element(By.XPATH, '//*[@id="dailypointToolTipDiv"]/p').text
        msg = f'[bing] rewards bot has netted {points} points for you today <3'
        send_discord_message(msg)
        points = driver.find_element(By.XPATH, '//*[@id="balanceToolTipDiv"]/p').text
        msg = f'[bing] now you have {points} points total.'
        send_discord_message(msg)
        
    except Exception as e:
        alert_discord_message('[bing] rewards bot failed in general')
        print(e)
    return driver

def bot():
    try:
        driver = init()
        driver = search(driver, initialize=True)
        driver = daily(driver)
        driver = alert_daily_reward(driver)
        driver.quit()
    except Exception as e:
        alert_discord_message('[bing] rewards bot failed in general')
        print(e)

def adv_bot():
    try:
        driver = init()
        for i in range(6):
            driver = search(driver, initialize=True, count=10)
            try:
                driver.quit()
                time.sleep(1800)
            except:
                pass
            driver = init()
        driver = daily(driver)
        driver = alert_daily_reward(driver)
        driver.quit()
    except Exception as e:
        alert_discord_message('[bing] rewards bot failed in general')
        print(e)
        raise
    return driver

if __name__ == "__main__":
    bot()
