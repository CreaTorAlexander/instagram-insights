import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM

# Complete these 2 fields ==================
USERNAME = 'XXXX'
PASSWORD = 'XXXX'
# ==========================================

TIMEOUT = 15


def scrape():
    # usr = input('[Required] - Whose followers do you want to scrape: ')
    usr = "XXXX"

    # user_input = int(
    #   input('[Required] - How many followers do you want to scrape (60-500 recommended): '))
    user_input = 50
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    bot.set_window_size(600, 1000)

    bot.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    print("[Info] - Logging in...")
    cookies = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//button[contains(text(),"Allow essential and optional cookies")]'))).click()

    
    user_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(USERNAME)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(5)

    bot.get('https://www.instagram.com/{}/'.format(usr))

    time.sleep(3.5)

    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, "//a[contains(@href, '/following')]"))).click()

    time.sleep(2)

    
    i = 0

    time.sleep(5)

    print('[Info] - Scrolling...')
    element_to_scroll = bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div[1]/div')
    print(element_to_scroll)
    # height variable
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        print("LAST HT ", last_ht)
        time.sleep(2)
        # scroll down and retrun the height of scroll
        ht = bot.execute_script(""" 
            element_to_scroll.scrollTo(0, element_to_scroll.scrollHeight);
            return element_to_scroll.scrollHeight; """, element_to_scroll)

        print("HT IS", ht)
        

    print('[Info] - Scraping...')
    
    # list follower name
    time.sleep(5)
    #print(f"{line} Scroll Buttom  Done!!! {line}")
    element_to_scroll = bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div[1]/div')
    links = element_to_scroll.find_elements_by_tag_name('a')
    time.sleep(2)
    names = [name.text for name in links if name.text != '']
    print(names)


    bot.close()

if __name__ == '__main__':
    scrape()
