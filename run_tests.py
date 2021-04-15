# -*- coding: utf-8 -*-

import unittest
import time

from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class EmailEmptyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testEmailEmpty(self):
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()
        self.assertIn('Войти', self.browser.title)

class PasswordEmptyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testPasswordEmpty(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('name')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()
        self.assertIn('Войти', self.browser.title)

class EmailMistakeTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testEmailMistake(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('name')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('pass')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

        error = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p#emailError')))
        self.assertIn('Do not find this user in db', error.get_attribute('innerText'))


class SendLetterTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testSendLetter(self):
        sendPage = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(2) > a')))
        sendPage.click()

        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div:nth-child(1) > input')))
        to.send_keys('mark@mailer.ru.com')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div:nth-child(2) > input')))
        theme.send_keys('Тема')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div.message.form-field > textarea')))
        message.send_keys('Сообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div.row > div:nth-child(1) > button')))
        button.click()
        self.assertIn('Письма', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
