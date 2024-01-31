import sys
import time
import pyperclip
from seleniumwire import webdriver
from seleniumwire.utils import decode
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from fake_useragent import UserAgent
from seleniumwire import webdriver
from seleniumwire.utils import decode
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

init()
def getkey(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    code_elements = soup.find_all('code', class_='aos-init aos-animate')
    if code_elements:
        return code_elements[0].text.strip()
    return None
def readhwid(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
def writehwid(filename, hwid):
    with open(filename, 'w') as file:
        file.write(hwid)
def gethwid():
    filename = "hwid"

    hwid = readhwid(filename)
    if hwid is not None: 
        return hwid
    else:
        print(Fore.MAGENTA + "")
        print(Fore.MAGENTA + "")
        print(Fore.MAGENTA + "")
        print(Fore.MAGENTA + "    ▄████████    ▄████████    ▄▄▄▄███▄▄▄▄   ▀████    ▐████▀ ")
        print(Fore.MAGENTA + "   ███    ███   ███    ███  ▄██▀▀▀███▀▀▀██▄   ███▌   ████▀ ")
        print(Fore.MAGENTA + "   ███    █▀    ███    ███  ███   ███   ███    ███  ▐███   ")
        print(Fore.MAGENTA + "  ▄███▄▄▄       ███    ███  ███   ███   ███    ▀███▄███▀ ")
        print(Fore.MAGENTA + " ▀▀███▀▀▀     ▀███████████  ███   ███   ███    ████▀██▄ ")
        print(Fore.MAGENTA + "   ███    █▄    ███    ███  ███   ███   ███   ▐███  ▀███ ")
        print(Fore.MAGENTA + "   ███    ███   ███    ███  ███   ███   ███  ▄███     ███▄ ")
        print(Fore.MAGENTA + "   ██████████   ███    █▀    ▀█   ███   █▀  ████       ███▄ ")
        print(Fore.MAGENTA + "")
        print(Fore.MAGENTA + "")
        print(Fore.MAGENTA + "")
        hwid = input("  Bypass HWID: ")
        writehwid(filename, hwid)
        print(Fore.GREEN + "Successful")
        return hwid
def main():
    hwid = gethwid()
    base_url = f"https://keysystem.fluxteam.net/android/checkpoint/start.php?HWID={hwid}"
    UA = UserAgent()
    agent = UA.random
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={agent}")
    options.add_argument("--window-size=500,500")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(base_url)
        driver.header_overrides = {'Referer': base_url}
        driver.get(f"{base_url}&7b20bcc1dfe26db966bb84f159da392f=false")
        driver.header_overrides = {'Referer': 'https://linkvertise.com'}
        driver.get("https://fluxteam.net/android/checkpoint/check1.php")
        driver.get("https://fluxteam.net/android/checkpoint/main.php")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'code')))
        body = driver.page_source
        key = getkey(body)
        print(Fore.GREEN + f"Successful Key: {key}")
        pyperclip.copy(key)
    except Exception as e:
        pass
    finally:
        driver.quit()
if __name__ == "__main__":
    main()
