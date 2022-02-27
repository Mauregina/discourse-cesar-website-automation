from selenium.webdriver.common.by import By
from automacao2.pages.PageObject import PageObject
from selenium.webdriver import ActionChains

class MenuPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_menu_school(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15376')).perform()

    def click_submenu_blog(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, 'menu-item-15254')).perform()
        action.click(on_element=self.driver.find_element(By.ID, 'menu-item-15254'))
        action.perform()
