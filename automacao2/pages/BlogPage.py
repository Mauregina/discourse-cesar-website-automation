import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from automacao2.pages.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC

class BlogPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_next_page(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primary']/div/nav/div/a[3]")))
        checkbox.click()

    def format_datetime_to_date(self, datatime: str) -> str:
        date = datatime.split('T')[0]
        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

    def get_article_list(self):
        return self.driver.find_element(By.ID, 'main').find_elements_by_tag_name("article")

    def get_article_title(self, post_order: int) -> str:
        article_info = self.get_article_list()[post_order-1]
        title_article = article_info.find_element_by_class_name("entry-title").text
        return title_article

    def get_article_date_published(self, post_order: int) -> str:
        article_info = self.get_article_list()[post_order-1]
        datetime_published = article_info.find_element_by_tag_name("time").get_attribute("datetime")
        date_published = self.format_datetime_to_date(datetime_published)
        return date_published

    def get_article_author(self, post_order: int) -> str:
        article_info = self.get_article_list()[post_order-1]
        author_article = article_info.find_element_by_class_name("author-name").text
        return author_article
