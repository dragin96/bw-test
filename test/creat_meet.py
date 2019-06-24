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
driver.get("https://feedback-j237750ea.dispatcher.ru1.hana.ondemand.com/#/meetings")

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
        Тест кейс создание встречи
    '''
    def test_a_creat_meating(self):
        self.element.click()
        self.fill_form()
        t.sleep(2)
        driver.find_element_by_id('save_meet').click()
        t.sleep(2)
        #сюда проверку что встреча создалась


    '''
        Тест кейс отмены
    '''
    def test_b_cancel_meat(self):
        self.element.click()
        self.fill_form()
        t.sleep(2)
        driver.find_element_by_id('cancel_meet').click()
        t.sleep(1)
        self.assertTrue(bool(1))

    '''
        Тест кейс изменит встречу
    '''
    def test_c_open_edit(self):
        self.open_sub_menu()
        actions_element = driver.find_element(By.CSS_SELECTOR, '.show-actions .meeting-actions__action--edit')
        self.action.move_to_element(actions_element).perform()
        actions_element.click()
        self.fill_form(4)
        driver.find_element_by_id('save_meet').click()


    @classmethod
    def tearDown(self):
        driver.get("https://feedback-j237750ea.dispatcher.ru1.hana.ondemand.com/#/meetings")

    '''
        Заполнение формы создание встречи
    '''
    def fill_form(self, date=4):
        t.sleep(4)
        driver.find_element_by_id('name-meet').send_keys('test meating')
        #
        select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#type-meet span'))
        )
        self.action.move_to_element(select).perform()
        t.sleep(1)
        select.click()
        t.sleep(1)
        driver.find_element_by_id('0_type').click()
        t.sleep(1)
        ###########
        driver.find_element_by_id('hour').click()
        t.sleep(2)
        driver.find_element_by_id('4_hour').click()
        t.sleep(1)
        ##########
        driver.find_element_by_id('min').click()
        t.sleep(2)
        driver.find_element_by_id('5_min').click()
        ##########
        t.sleep(2)
        driver.find_element_by_css_selector('[aria-label="Open calendar"]').click()
        t.sleep(5)
        print(get_date(10))
        driver.find_element_by_css_selector('[aria-label="' + get_date(date) + '"]').click()

    '''
        Открыть меню встречи
    '''
    def open_sub_menu(self):
        t.sleep(2)
        el = driver.find_elements_by_css_selector('.meeting__actions > #meet-action')[0]
        el.click()
        t.sleep(4)

if __name__ == '__main__':
    unittest.main()