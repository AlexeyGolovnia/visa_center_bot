import time
from datetime import datetime
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options=Options()
# options.add_argument('-headless')
firefox_profile = FirefoxProfile('c:/Users/51050/AppData/Roaming/Mozilla/Firefox/Profiles/tgq19mwq.default')
options.profile = firefox_profile

token = '*********************************'
url = 'https://api.telegram.org/bot'
channel_id = '*****************'
url += token
method = url + '/sendMessage'

t = {'//*[@id="mat-option-0"]': ('Самый ранний доступный слот записи : 22-08-2023', 'Karta Polaka D-visa'), #baranovichi
     '//*[@id="mat-option-1"]': ('Самый ранний доступный слот записи : 22-08-2023', 'Karta Polaka D-visa'), #brest
     '//*[@id="mat-option-2"]': ('Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже', 'D - National Visa'), #gomel
     '//*[@id="mat-option-3"]': ('Самый ранний доступный слот записи : 31-08-2023', 'Karta Polaka D-visa'), #grodno
     '//*[@id="mat-option-4"]': ('Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже', 'Karta Polaka D-visa'), #lida
     '//*[@id="mat-option-5"]': ('Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже', 'D - National Visa'), #minsk
     '//*[@id="mat-option-6"]': ('Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже', 'D - National Visa'), #mogilev
     '//*[@id="mat-option-7"]': ('Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже', 'Karta Polaka D-visa') #pinsk
     }

def req(text):
    requests.post(method, data={
        'chat_id': channel_id,
        'text': text
        })

def action_click(driver, xpath, action, keys):
    tmp = 0
    while True:
        try:
            time.sleep(0.5)
            element = driver.find_element(By.XPATH, xpath)
            if action == 0:
                element.click()
            if action == 1:
                element.send_keys(keys)
            return 1
        except:
            tmp += 1
            if tmp == 40:
                return 0

def first_page():
    tmp = 0
    while True:
        try:
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "c-brand-blue")
            print('!!!!', datetime.now().strftime("%H:%M:%S"))
            return 0
        except:
            if tmp == 15:
                break
            tmp += 1

    action_click(driver, "//*[@id='mat-input-0']", 1, '***************@gmail.com')
    action_click(driver, "//*[@id='mat-input-1']", 1, '************')

    try:
        req('ввести капчу!')
    except:
        ()

    input('прежде чем нажать ввод: ввести капчу, нажать войти.')

    action_click(driver, "/html/body/app-root/div/app-dashboard/section[1]/div/div[2]/button", 0, None)
    return 1

def second_page():
    tmp = 0

    while True:
        for key, value in t.items():
            print(len(driver.get_cookies()), 'cookies')
            # city
            action_click(driver, "//*[@id='mat-select-value-1']", 0, None)
            action_click(driver, key, 0, None)

            # category
            action_click(driver, '//*[@id="mat-select-value-3"]', 0, None)
            action_click(driver, "//*[contains(text(), 'National Visa D')]", 0, None)

            # subcategory
            action_click(driver, '//*[@id="mat-select-value-5"]', 0, None)
            action_click(driver, f"//*[contains(text(), '{value[1]}')]", 0, None)

            # birthday
            a = action_click(driver, '//*[@placeholder = "ДД/ММ/ГГГГ"]', 1, "**/**/****")
            if a == 0:
                return 0

            # nationality
            action_click(driver, '//*[@id = "mat-select-value-7"]', 0, None)
            action_click(driver, "//*[contains(text(), 'BELARUS')]", 0, None)

            time.sleep(0.5)

            vyvod = driver.find_element(By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[6]/div')
            text = vyvod.text
            tmp += 1
            print(tmp, text, datetime.now().strftime("%H:%M:%S"))
            if text != value[0] and text != 'Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже':
                return 1

        time.sleep(120)

def registration():
    action_click(driver, "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button", 0, None)
    action_click(driver, '//*[@placeholder = "Введите Идентификационный номер"]', 1, "********************")
    action_click(driver, '//*[@placeholder = "Введите свое имя"]', 1, "********")
    action_click(driver, '//*[@placeholder = "Пожалуйста, введите фамилию."]', 1, "********")
    action_click(driver, '//*[@placeholder = "Введите номер паспорта"]', 1, "**********")
    action_click(driver, '//*[@placeholder = "44"]', 1, "29")
    action_click(driver, '//*[@placeholder = "012345648382"]', 1, "**********")
    action_click(driver, '//*[@placeholder = "Введите адрес электронной почты"]', 1, "****************@GMAIL.COM")
    action_click(driver, "//*[@id='mat-select-8']", 0, None)
    action_click(driver, "//*[contains(text(), 'Male')]", 0, None)
    action_click(driver, '//*[@placeholder = "ДД / ММ / ГГГГ"]', 1, "**")
    action_click(driver, '//*[@placeholder = "ДД / ММ / ГГГГ"]', 1, "**")
    action_click(driver, '//*[@placeholder = "ДД / ММ / ГГГГ"]', 1, "****")

def msi():
    action_click(driver2, '//*[@placeholder = "1111111A111AA1"]', 1, "*******************")
    action_click(driver2, '//*[@placeholder = "+375XXXXXXXXX"]', 1, "+****************")
    action_click(driver2, "/ html / body / div / div / form / fieldset / div[4] / button[1]", 0, None)


while True:
    driver = webdriver.Firefox(options=options)
    driver.get("https://visa.vfsglobal.com/blr/ru/pol/login")
    a = first_page()
    if a == 1:
        b = second_page()
        if b == 1:
            driver2 = webdriver.Firefox(options=options)
            driver2.get("https://ticketing.raschet.by/vfs/web/login")
            msi()
            registration()
            break
        if b == 0:
            driver.close()
            continue
    if a == 0:
        driver.close()
        time.sleep(120)
        continue
