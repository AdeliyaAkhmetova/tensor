import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from base.base_page import BasePage


class Test_2(BasePage):
    def page_opening_2(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        print("Start test2")

        """Нажатие клавиши Контакты"""

        wait = WebDriverWait(self.driver, 10)
        button_contact_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='wasaby-content']/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a")))
        button_contact_element.click()
        print("Нажатие клавиши КОНТАКТЫ")

        """Сравнение регионов"""

        region_element = self.driver.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")

        # Проверяем, что текст региона соответствует ожидаемому значению
        expected_region = "Республика Крым"
        actual_region = region_element.text

        if actual_region == expected_region:
            print(f"Регион соответствует ожидаемому: {expected_region}")
        else:
            print(f"Регион не соответствует ожидаемому. Ожидался {expected_region}, но получено {actual_region}")

        try:
            element = self.driver.find_element(By.ID, "contacts_list")
            print("Список партнеров найден")
        except NoSuchElementException:
            print("Список партнеров не найден")

        """Изменение региона"""
        region_button = self.driver.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
        region_button.click()
        time.sleep(2)
        region_kamchatka_button = self.driver.find_element(By.XPATH,
                                                           "//*[@id='popup']/div[2]/div/div[2]/div/ul/li[43]/span")
        region_kamchatka_button.click()
        time.sleep(2)

        """Проверка title"""
        expected_title = "СБИС Контакты — Камчатский край"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print(f"Заголовок страницы совпадает: {actual_title}")
        else:
            print(f"Заголовок страницы не совпадает. Ожидался: {expected_title}, Фактический: {actual_title}")

        """Проверка URL"""
        expected_region = "kamchatskij-kraj"
        current_url = self.driver.current_url

        if expected_region in current_url:
            print(f"URL содержит информацию о регионе {expected_region}")
        else:
            print(f"URL не содержит информацию о регионе {expected_region}")

        time.sleep(3)
        self.driver.quit()


test = Test_2()
test.page_opening_2()

