from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t
from datetime import datetime, date, time, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def get_date(n = 0):
    current_date = datetime.now()
    res = current_date.date() if n==0 else (current_date + timedelta(days=n))
    return res.strftime("%d %B %Y г.")


class TestComite(object):
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--args")
        chrome_options.add_argument("--disable-web-security")
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        self.driver.get("localhost:4200")
        self.date_calendar = get_date(1)
        self.navigation()

    def navigation(self):
        self.driver.save_screenshot('0.png')
        self.driver.find_element_by_css_selector('.sub-router > .sub-router__tile:nth-child(3)').click()
        #
        self.driver.save_screenshot('1.png')
        self.driver.find_element_by_css_selector('.sub-router > .sub-router__tile:nth-child(1)').click()
        t.sleep(4)
        self.driver.find_element_by_css_selector("[routerlink='/dashboard/kk/talents-committee/create-new']").click()
        t.sleep(2)
        self.driver.find_element_by_css_selector('[placeholder="Название комитета"]').send_keys('новый')
        self.driver.find_element_by_css_selector('[placeholder="Трайб"]').send_keys('360')
        self.driver.find_element_by_css_selector('[placeholder="Трайб"]').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_css_selector('[placeholder="Трайб"]').send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector('#date1 [aria-label="Open calendar"]').click()
        self.driver.find_element_by_css_selector('[aria-label="' + get_date(1) + '"]').click()
        t.sleep(2)
        self.driver.find_element_by_css_selector('#date2 [aria-label="Open calendar"]').click()
        self.driver.find_element_by_css_selector('[aria-label="' + get_date(4) + '"]').click()
        t.sleep(2)
        self.driver.find_element_by_css_selector('#date4 [aria-label="Open calendar"]').click()
        self.driver.find_element_by_css_selector('[aria-label="' + get_date(5) + '"]').click()
        t.sleep(2)
        self.driver.find_element_by_css_selector('#date6 [aria-label="Open calendar"]').click()
        self.driver.find_element_by_css_selector('[aria-label="' + get_date(6) + '"]').click()
        t.sleep(2)
        self.driver.find_element_by_css_selector('#date8 [aria-label="Open calendar"]').click()
        self.driver.find_element_by_css_selector('[aria-label="' + get_date(7) + '"]').click()

        self.driver.find_element_by_css_selector('.create-new__buttons-wrap > button.mat-flat-button').click()
        t.sleep(1000)
        print(self.driver.get_log('browser'))
        print(1111111)


# driver.close()
# driver.quit()

TestComite()

