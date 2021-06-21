import threading
from time import sleep

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def start(url):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    with Chrome(options=options, executable_path='c:\\WebDriver\\bin\\chromedriver.exe') as driver:
        driver.get(url)
        WebDriverWait(driver, 1000)
        sleep(2)
        driver.find_element_by_id('s2id_provinceCd').click()
        driver.find_element_by_id('s2id_autogen1_search').send_keys('4' + Keys.ENTER)
        sleep(4)
        driver.find_element_by_class_name('close').click()
        sleep(4)
        driver.find_element_by_partial_link_text('Book now for Driving Licence Card ').click()
        sleep(10)
        # Driver details.
        driver.find_element_by_class_name('select2-arrow').click()
        driver.find_element_by_id('idDocTypeCd').send_keys('02' + Keys.ENTER)
        driver.find_element_by_id('idDocN').send_keys('')
        driver.find_element_by_id('surname').send_keys('')
        driver.find_element_by_id('initials').send_keys('')
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        input("Press any button to close the browser - make sure you are done with this submission")


if __name__ == '__main__':
    start('https://online.natis.gov.za/#/')
