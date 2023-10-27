import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from base.base_page import BasePage
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_1(BasePage):

    def page_opening_1(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        print("Start test")
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        button_contact_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='wasaby-content']/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a")))
        button_contact_element.click()
        print("Нажатие клавиши КОНТАКТЫ")
        button_tensor_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contacts_clients']/div[1]/div/div/div[2]/div/a/img")))
        button_tensor_element.click()
        time.sleep(2)

        print("Нажатие на баннер ТЕНЗОР")
        original_window = self.driver.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        current_url = self.driver.current_url
        # Сравнение URL
        if current_url == self.tensor_url:
            print("URL совпадает")
        else:
            print(f"URL не совпадает. Текущий URL: {current_url}")
        force_people = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='container']/div[1]/div/div[5]/div")))
        action = ActionChains(self.driver)
        action.move_to_element(force_people).perform()
        print("Перемещено к элементу")
        """Сравнение подписей"""
        heading_force_people = self.driver.find_element(By.CSS_SELECTOR,"#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16")
        assert heading_force_people.text == "Сила в людях"
        print("Блок 'Сила в людях' присутствует")
        details = self.driver.find_element(By.CSS_SELECTOR,"#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")
        details.click()
        time.sleep(5)
        print("Переход в 'Подробнее...'")
        # Работа в tensor.ru/about
        working = self.driver.find_element(By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")
        # Сравнение URL
        wait = WebDriverWait(self.driver, 10)

        try:
            redirected_url = wait.until(EC.url_to_be(self.tensor_about_url))
            print(f"Перенаправлен на {redirected_url}")
        except TimeoutException:
            print("Время ожидания истекло. Перенаправление не произошло.")

            print(redirected_url)

        action = ActionChains(self.driver)
        action.move_to_element(working).perform()
        # Проверка фотографий по ширине и высоте
        photos_section = self.driver.find_element(By.CSS_SELECTOR, ".s-Grid-container")
        # Найти все изображения внутри этого контейнера
        images = photos_section.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block3-image-filter")
        first_image_width = first_image_height = None
        # Проверяем размеры первой фотографии
        if images:
            first_image_width = images[0].size['width']
            first_image_height = images[0].size['height']

        # Проверяем все остальные фотографии
        for image in images[1:]:
            width = image.size['width']
            height = image.size['height']

            if width != first_image_width or height != first_image_height:
                print(f'Фотографии имеют разные размеры!')
                break

        # Если код дошел до этого места, значит все фотографии имеют одинаковые размеры
        print("Размеры фото совпадают")


        time.sleep(3)
        self.driver.quit()



test = Test_1()
test.page_opening_1()
# test.page_opening_2()

