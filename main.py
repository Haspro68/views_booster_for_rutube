import sys
import time
import concurrent.futures
import random

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
#from selenium.webdriver.common.by import By

user_agents = [
    'hello',
    'Mozilla/5.0 (Linux; Android 9; EVR-AL00 Build/HUAWEIEVR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.1.332 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 8.0.0; en-gb; SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 PHX/14.7',
]
#url, duration = str(sys.argv[1]), int(sys.argv[2])
#url = 'https://2ip.ru/'
url = 'https://whatmyuseragent.com/'
duration = 20
proxies = []
try:
    with open('proxy_file.txt', 'r') as file:
        proxies=file.readlines()
except:
    print('Error')
print('Total proxies: ', len(proxies))


def view_boost(proxy):
    options = ChromeOptions()
    options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    #options.add_argument('window-size=640, 480')

    try:
        service = ChromeService(executable_path='/usr/bin/chromedriver')
        driver = Chrome(options=options, service=service)
        driver.get(url)
        time.sleep(duration)
    except:
        pass

    driver.quit()


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(view_boost, proxies)
