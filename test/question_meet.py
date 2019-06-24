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
chrome_options.add_argument("--args")
chrome_options.add_argument("--disable-web-security")
driver = webdriver.Chrome('./chromedriver 2', chrome_options=chrome_options)
driver.get("localhost:4200")

class  QuestionMeting(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.action = ActionChains(driver)
        inst.element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'creat-meet'))
        )
        t.sleep(2)

    def fill_question(self, type):
        t.sleep(1)
        driver.find_element_by_css_selector('[tid="creat-question"]').click()
        t.sleep(1)
        driver.find_element_by_id('type-question').click()
        t.sleep(1)
        driver.find_element_by_id(str(type) + '_questionTypes').click()
        t.sleep(1)
        driver.find_element_by_id('name-question').send_keys('Как победить баги?')
        t.sleep(1)
        i = 0
        while i < 3:
            driver.find_element_by_id(str(i) + '_answer').send_keys('как?' + str(i))
            t.sleep(1)
            i = i + 1
            if i < 3:
                driver.find_element_by_id('add-question').click()
        t.sleep(1)
        driver.find_element_by_id('save_qustion').click()
        t.sleep(2)


    '''
       Тест кейс по добавление вопроса(c одним ответом) 
    '''
    def test_a_add_question(self):
        t.sleep(1)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()  # поченить
        t.sleep(2)
        driver.find_element_by_id('1_nav-header').click()
        self.fill_question(0)
        qustion = driver.find_element_by_id('title-question').text
        self.assertEqual(qustion, 'Как победить баги?')
        answer = driver.find_elements_by_css_selector('#group_answer .qa__list-item')
        last_answer = answer[len(answer) - 1].text.split('. ')[1]
        self.assertEqual(last_answer, 'Не могу ответить')
        self.answer_question(self, 1)

    '''
        Тест кейс по добавление вопроса(c несколько ответом) 
     '''

    def test_b_add_question(self):
        t.sleep(1)
        driver.find_element_by_css_selector('.meetings__item:nth-child(1) .meeting').click()  # поченить
        t.sleep(2)
        driver.find_element_by_id('1_nav-header').click()
        self.fill_question(1)
        qustion = driver.find_element_by_id('title-question').text
        self.assertEqual(qustion, 'Как победить баги?')
        answer = driver.find_elements_by_css_selector('#group_answer .qa__list-item')
        last_answer = answer[len(answer) - 1].text.split('. ')[1]
        self.assertEqual(last_answer, 'Не могу ответить')
        t.sleep(2)
        self.answer_question(self, 2)

    def test_c_deleted_question(self):# TODO: удаление 
        t.sleep(1)
        driver.find_elements_by_css_selector('.meetings__item:nth-child(1) .meeting')[1].click()  # поченить
        t.sleep(2)
        driver.find_element_by_id('1_nav-header').click()
        t.sleep(2)
        question = driver.find_elements_by_css_selector('.question__trigger')[0]
        self.action.move_to_element(question)
        question.click()
        driver.find_element_by_css_selector('.question-button__action--remove').click()


    '''
        Отвечает на вопрос
        @:param num кол-во ответов
    '''
    @staticmethod
    def answer_question(this, num):
        i = 0
        while i < num:
            driver.find_element_by_id(str(i) + '_answer').click()
            i = i + 1
            t.sleep(1)

        driver.find_element_by_id('comment-answer').send_keys('коментарии')
        t.sleep(1)
        save_answer = driver.find_element_by_id('send-answer')
        this.action.move_to_element(save_answer)
        save_answer.click()
        t.sleep(3)
        driver.find_element_by_css_selector('.global-popup-message.active-msg .global-popup-message__desc')
        popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.global-popup-message.active-msg'
                                                             ' .global-popup-message__desc'))
        )
        t.sleep(2)

    @classmethod
    def tearDown(self):
        driver.get("localhost:4200")

if __name__ == '__main__':
    unittest.main()