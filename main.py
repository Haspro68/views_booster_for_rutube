import time
import concurrent.futures
import random
from settings import deep_view, url

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By


url = url
duration = deep_view
proxies = []
user_agents = []
logins = []
passwords = []
accounts = []
acc_dict = {}


try:
    with open('accounts.txt', 'r') as ac:
        accounts = ac.readlines()
    for elem in accounts:
        logins.append(elem.split(';')[0])
        passwords.append(elem.strip().split(';')[1])
    acc_dict = {logins[i]: passwords[i] for i in range(len(logins))}
except:
    pass


try:
    with open('proxy_file.txt', 'r') as file:
        proxies=file.readlines()
except:
    print('Error')
print('Total proxies: ', len(proxies))


try:
    with open('user_agents.txt', 'r') as users:
        user_agents=users.readlines()
except:
    print('Error')
print('Total user agents: ', len(user_agents))


def view_boost(proxy):
    options = ChromeOptions()
    options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    options.add_argument('window-size=640, 480')

    try:
        service = ChromeService(executable_path='/usr/bin/chromedriver')
        driver = Chrome(options=options, service=service)
        driver.get(url)
        ####
        ####
        time.sleep(duration)
    except:
        pass

    driver.quit()


def view_boost_with_account(proxy):
    options = ChromeOptions()
    options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    options.add_argument('window-size=640, 480')

    try:
        service = ChromeService(executable_path='/usr/bin/chromedriver')
        driver = Chrome(options=options, service=service)
        driver.get(url)
        login = random.choice(list(acc_dict))
        time.sleep(10)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/header/section[2]/div[4]/button')
        button.click()
        time.sleep(20)
        login_input = driver.find_element(by=By.ID, value='phone-or-email-login')
        login_input.clear()
        login_input.send_keys(login)
        submit_login = driver.find_element(by=By.ID, value='submit-login-continue')
        submit_login.click()
        time.sleep(5)
        password_input = driver.find_element(by=By.ID, value='login-password')
        password_input.clear()
        password_input.send_keys(acc_dict[login])
        submit_login_final = driver.find_element(by=By.ID, value='submit-login')
        submit_login_final.click()
        time.sleep(5)
        activity_or_not = random.randint(0, 1)
        if activity_or_not == 0:
            time.sleep(duration)
            driver.quit()
        else:
            time.sleep(duration)
            like = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section')
            like.click()
            time.sleep(1)
            subscribe = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[2]/div/div/div[2]/div/button')
            subscribe.click()
            time.sleep(2)
            driver.quit()
    except:
        pass



#for _ in range(count):
#   log_or_no = random.randint(0, 1)
#    if log_or_no == 0:
#        with concurrent.futures.ThreadPoolExecutor() as executor:
#            executor.map(view_boost, proxies)
#    else:
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(view_boost_with_account, proxies)
