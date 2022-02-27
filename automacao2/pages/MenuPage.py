from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from automacao2.pages.PageObject import PageObject
from selenium.webdriver import ActionChains

class MenuPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_menu_page_displayed(self) -> bool:
        try:
            return self.driver.find_element(By.ID, 'primary-menu') != 0

        except NoSuchElementException:
            return False

    def is_menu_school_displayed(self) -> bool:
        try:
            return self.driver.find_element(By.ID, 'menu-item-15376') != 0

        except NoSuchElementException:
            return False

    def is_submenu_blog_displayed(self) -> bool:
        try:
            return self.driver.find_element(By.ID, 'menu-item-15254') != 0

        except NoSuchElementException:
            return False

    def open_menu_school(self):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15376')).perform()

        except NoSuchElementException:
            return

    def click_submenu_blog(self):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15254')).perform()
            action.click(on_element=self.driver.find_element(By.ID, 'menu-item-15254'))
            action.perform()

        except NoSuchElementException:
            return
