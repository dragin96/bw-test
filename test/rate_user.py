from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest
import time as t
from datetime import datetime, date, time, timedelta
import locale
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')



chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--user-data-dir="/Users/dragin/Library/Application Support/Google/Chrome/Default"')
chrome_options.add_argument("--args")
chrome_options.add_argument("--disable-web-security")
driver = webdriver.Chrome('./chromedriver 2', chrome_options=chrome_options)
driver.get("localhost:4200")

def get_date(n=0):
    current_date = datetime.now()
    res = current_date.date() if n==0 else (current_date + timedelta(days=n))
    return res.strftime("%a %B %d %Y")


class CreatMeting(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.action = ActionChains(driver)
        inst.element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'creat-meet'))
        )
        t.sleep(2)

    '''
        Выставление оценки
    '''
    def test_add_rate(self):
        t.sleep(1)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()  # поченить
        t.sleep(2)
        user = driver.find_elements_by_css_selector('app-rtf-participant')[1]
        user.click()
        t.sleep(3)
        element = driver.find_element_by_css_selector('.mat-slider')
        self.action.click_and_hold(element).move_by_offset(-200, 0).move_by_offset(200,0).release().perform()
        driver.find_element_by_id('1_1_desc-list').click()
        driver.find_element_by_id('save-result').click()
        t.sleep(2)


    @classmethod
    def tearDown(self):
        driver.get("localhost:4200")


if __name__ == '__main__':
    unittest.main()