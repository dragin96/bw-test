from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import unittest
import time as t
from datetime import datetime, date, time, timedelta
import locale
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--args")
chrome_options.add_argument("--disable-web-security")
driver = webdriver.Chrome('./chromedriver 2', chrome_options=chrome_options)
driver.get("https://bridgewater-j237750ea.dispatcher.ru1.hana.ondemand.com/#/meetings")

class UsertMeting(unittest.TestCase):

    @classmethod
    def setUp(inst):
        inst.action = ActionChains(driver)
        inst.element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'creat-meet'))
        )
        t.sleep(2)

    '''
        Добавить юзера во встречу
    '''
    def add_participant(self, user):
        driver.find_element_by_css_selector('.search__input--add').send_keys(user)
        t.sleep(6)
        driver.find_element_by_css_selector('.search__result:nth-child(1) > .search__result-name').click()
    '''
        Тест кейс для добавлению юзеров(много)
    '''
    def test_a_add_many_participant(self):
        t.sleep(2)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()
        t.sleep(2)
        before_item_len = len(driver.find_elements_by_css_selector('#items-participants app-rtf-participant'))
        # users = ['Михаил', 'Максим', 'Артем', 'Даниил', 'Иван', 'Дмитрий', 'Марк', 'Матвей', 'Илья']*2
        users = ['Миха', 'Макс', 'Арте']*3
        for name in users:
            self.add_participant(name)
        t.sleep(3)
        items_user = driver.find_elements_by_css_selector('#items-participants app-rtf-participant')
        self.assertTrue(len(users)+before_item_len == len(items_user))

    '''
        Закрепить юзера во встречи
        @:param type number
    '''
    def pin_user(self, utype = 1):
        if utype == 1:
            user = driver.find_elements_by_css_selector('.unpin')[1]
        else:
            user = driver.find_elements_by_css_selector('.pined')[0]
        self.action.move_to_element(user)
        t.sleep(3)
        user.find_element_by_css_selector('.button__trigger').click()
        t.sleep(2)
        user.find_element_by_id('pin').click()
        t.sleep(2)
    '''
        Закрепить юзера во встречи(много)
    '''
    def test_b_pin_many_user(self):
        pin_num = 3
        t.sleep(2)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()  # поченить
        t.sleep(2)
        before_item_len = len(driver.find_elements_by_css_selector('#items-participants app-rtf-participant .pin'))
        i = 0
        while i < pin_num:
            self.pin_user(1)
            i = i + 1
        t.sleep(3)
        items_user = driver.find_elements_by_css_selector('#items-participants app-rtf-participant .pin')
        self.assertTrue(before_item_len + pin_num == len(items_user))

    def test_c_unpin(self):
        t.sleep(2)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()  # поченить
        t.sleep(2)
        before_item_len = len(driver.find_elements_by_css_selector('#items-participants app-rtf-participant .pined'))
        self.pin_user(2)


    '''
        Удаления юзеров
    '''
    def deleted_participant(self):
        user = driver.find_elements_by_css_selector('app-rtf-participant .unpin')[1]
        t.sleep(1)
        self.action.move_to_element(user)
        t.sleep(3)
        user.find_element_by_css_selector('.button__trigger').click()
        t.sleep(2)
        user.find_element_by_id('remove').click()
        t.sleep(2)


    '''
        Тест кейс для удаления юзеров во встречи (много) 
    '''
    def test_c_deleted_many_participant(self):
        DELET_NUM = 3
        t.sleep(2)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click() #поченить
        t.sleep(2)
        before_item_len = len(driver.find_elements_by_css_selector('#items-participants app-rtf-participant'))
        i = 0
        while i < DELET_NUM:
            self.deleted_participant()
            i = i+1
        t.sleep(3)
        items_user = driver.find_elements_by_css_selector('#items-participants app-rtf-participant')
        self.assertTrue(before_item_len-DELET_NUM == len(items_user))


    @classmethod
    def tearDown(self):
        driver.get("https://feedback-j237750ea.dispatcher.ru1.hana.ondemand.com/#/meetings")

if __name__ == '__main__':
    unittest.main()