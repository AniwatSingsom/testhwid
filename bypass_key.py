from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import pyperclip
from colorama import Fore, Back, Style, init

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
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android',
        'app': '/path/to/appium-apk-file.apk',
        'appPackage': 'com.fluxteam.keysystem',
        'appActivity': '.MainActivity',
        'noReset': 'true',
        'userAgent': agent
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        driver.get(base_url)
        driver.header_overrides = {'Referer': base_url}
        driver.get(f"{base_url}&7b20bcc1dfe26db966bb84f159da392f=false")
        driver.get("https://fluxteam.net/android/checkpoint/check1.php")
        driver.get("https://fluxteam.net/android/checkpoint/main.php")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'code')))
        body = driver.page_source
        key = getkey(body)
        print(Fore.GREEN + f"Successful Key: {key}")
        pyperclip.copy(key)
    except Exception as e:
