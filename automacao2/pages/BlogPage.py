import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from automacao2.pages.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC

class BlogPage(PageObject):
    URL_BLOG = 'https://www.cesar.school/blog/'
    txt_page_title = 'blog'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_blog_page(self) -> bool:
        return self.driver.current_url == self.URL_BLOG

    def is_blog_page(self) -> bool:
        try:
            blog_class_title = self.driver.find_element_by_xpath('//*[@id="page"]/div[1]/div/div/div/nav/div/ul/li[2]/span/span').text.lower()

            articles_list = self.get_article_list()

            return blog_class_title == self.txt_page_title and articles_list

        except NoSuchElementException:
            return False

    def is_pagination_displayed(self) -> bool:
        try:
            return self.driver.find_element(By.XPATH, '//*[@id="primary"]/div/nav/div/a[3]') != 0

        except NoSuchElementException:
            return False

    def is_next_page(self) -> bool:
        try:
            return self.driver.find_element(By.XPATH, '//*[@id="page"]/div[1]/div/div/div/nav/div/ul/li[3]/span/span') != 0

        except NoSuchElementException:
            return False

    def click_next_page(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="primary"]/div/nav/div/a[3]')))
            checkbox.click()

        except NoSuchElementException:
            return

    def format_datetime_to_date(self, datatime: str) -> str:
        date = datatime.split('T')[0]
        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

    def get_article_list(self) -> list:
        try:
            return self.driver.find_element(By.ID, 'main').find_elements_by_tag_name("article")
        except NoSuchElementException:
            return None

    def get_article_title(self, post_order: int) -> str:
        try:
            article_info = self.get_article_list()[post_order-1]
            title_article = article_info.find_element_by_class_name("entry-title").text
            return title_article

        except NoSuchElementException:
            return ''

    def get_article_date_published(self, post_order: int) -> str:
        try:
            article_info = self.get_article_list()[post_order-1]
            datetime_published = article_info.find_element_by_tag_name("time").get_attribute("datetime")
            date_published = self.format_datetime_to_date(datetime_published)
            return date_published

        except NoSuchElementException:
            return ''

    def get_article_author(self, post_order: int) -> str:
        try:
            article_info = self.get_article_list()[post_order-1]
            author_article = article_info.find_element_by_class_name("author-name").text
            return author_article

        except NoSuchElementException:
            return ''