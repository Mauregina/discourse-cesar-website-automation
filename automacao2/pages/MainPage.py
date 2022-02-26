import datetime
import time

from selenium.webdriver.common.by import By
from collections import Counter

from selenium.webdriver.support.wait import WebDriverWait

from automacao2.pages.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class MainPage(PageObject):
    URL_MAIN = 'https://www.cesar.school/'
    txt_demo = 'Demo'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_main_page_url()

    def open_main_page_url(self):
        self.driver.get(self.URL_MAIN)

    def is_url_main_page(self):
        return self.driver.current_url == self.URL_MAIN

    def open_menu_school(self):
        #cookies
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/a[2]'))).click()

        #abrir menu school
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15376')).perform()

        action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15254')).perform()
        action.click(on_element=self.driver.find_element(By.ID, 'menu-item-15254'))
        action.perform()

        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primary']/div/nav/div/a[3]")))
        checkbox.click()

        #DESAFIO 4
        posts = self.driver.find_element(By.ID, 'main')

        articles = posts.find_elements_by_tag_name("article")
        second_article = articles[1]

        datetime_published = second_article.find_element_by_tag_name("time").get_attribute("datetime")
        title_second_article = second_article.find_element_by_class_name("entry-title").text

        #criar funcao --------------------------------------------
        date_published_text = datetime_published.split('T')[0]
        date_published = datetime.datetime.strptime(date_published_text, "%Y-%m-%d").strftime("%d/%m/%Y")
        #---------------------------------------------------------

        print(date_published)
        print(title_second_article)

        #DESAFIO 5
        third_article = articles[2]
        title_third_article = third_article.find_element_by_class_name("entry-title").text

        x = third_article.find_element_by_class_name("author-name").text

        print(title_third_article)
        print(x)

        #DESAFIO 6

        #criar metodo ----------------------------------------------------
        scroll_pause_time = 2

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height
        #------------------------------------------------------------------------------

        address = self.driver.find_element_by_class_name('onde').find_element_by_tag_name('p').text

        print(address)
































