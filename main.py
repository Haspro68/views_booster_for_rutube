import time
import concurrent.futures
import random
from settings import deep_view, url, max_workers, path
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


url = url
duration = deep_view
proxies = []
user_agents = []
logins = []
passwords = []
accounts = []
reactions = [
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[1]/div/span',
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[2]/div/span',
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[3]/div/span',
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[4]/div/span',
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[5]/div/span',
    '/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section/div[1]/div[2]/div[2]/div[2]/div[6]/div/span'
]


try:
    with open('accounts.txt', 'r') as ac:
        accounts = ac.readlines()
    for elem in accounts:
        logins.append(elem.split(';')[0])
        passwords.append(elem.strip().split(';')[1])
except Exception as exc:
    print(exc)

try:
    with open('proxy_file.txt', 'r') as file:
        proxies=file.readlines()
except Exception as exc:
    print(exc)
print('Total proxies: ', len(proxies))


try:
    with open('user_agents.txt', 'r') as users:
        user_agents=users.readlines()
except Exception as exc:
    print(exc)
print('Total user agents: ', len(user_agents))


def view_boost_with_account(proxy, login, password):
    options = ChromeOptions()
    options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    try:
        #указать полный путь до chromedriver
        service = ChromeService(
            executable_path=path)
        driver = Chrome(options=options, service=service)
        driver.get(url)
        driver.implicitly_wait(10)
        if not driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/header/section[1]/section/a'):
            driver.close()
            driver.quit()
        driver.maximize_window()
        try:
            agree_cookie = driver.find_element(by=By.XPATH, value='/html/body/div[4]/aside/noindex/div/div[2]/button')
            agree_cookie.click()
        except NoSuchElementException:
            pass
        driver.implicitly_wait(2)
        try:
            close = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div[1]/button')
            close.click()
        except NoSuchElementException:
            pass
        log_or_no = random.randint(0, 1)
        if log_or_no == 0:
            try:
                time.sleep(duration)
                driver.close()
                driver.quit()
            except Exception as exc:
                print(exc)
            finally:
                driver.close()
                driver.quit()
        else:
            try:
                button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/header/section[2]/div[4]/button')
                button.click()
                frame = driver.find_element(by=By.ID, value='snake-popup')
                driver.switch_to.frame(frame)
                driver.implicitly_wait(5)
                login_input = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div/div[2]/form/div[1]/div/input')
                login_input.send_keys(login)
                driver.implicitly_wait(5)
                submit_login = driver.find_element(by=By.ID, value='submit-login-continue')
                submit_login.click()
                driver.implicitly_wait(20)
                password_input = driver.find_element(by=By.ID, value='login-password')
                password_input.clear()
                password_input.send_keys(password)
                submit_login_final = driver.find_element(by=By.ID, value='submit-login')
                submit_login_final.click()
                driver.implicitly_wait(5)
                try:
                    driver.find_element(by=By.TAG_NAME, value='form').click()
                    like_popup = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/form/div/div[1]/button')
                    like_popup.click()
                except NoSuchElementException:
                    pass
                try:
                    driver.find_element(by=By.TAG_NAME, value='form').click()
                    like_popup_side = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/form/div/div[1]/button')
                    like_popup_side.click()
                except NoSuchElementException:
                    pass
                time.sleep(5)
                activity_or_not = random.randint(0, 1)
                if activity_or_not == 0:
                    time.sleep(duration)
                    driver.close()
                    driver.quit()
                else:
                    time.sleep(duration)
                    driver.execute_script("window.scrollBy(0, 500)")
                    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div').click()
                    like = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[1]/div[2]/section')
                    like.click()
                    time.sleep(5)
                    react = driver.find_element(by=By.XPATH, value=random.choice(reactions))
                    react.click()
                    time.sleep(2)
                    subscribe = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div/main/div[1]/div[1]/section/div/div[1]/section[2]/div/div/section[2]/div/div/div[2]/div/button')
                    subscribe.click()
                    time.sleep(2)
                    driver.close()
                    driver.quit()
            except Exception as exc:
                print(exc)
            finally:
                driver.close()
                driver.quit()
    except Exception as exc:
        print(exc)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        executor.map(view_boost_with_account, proxies, logins, passwords)