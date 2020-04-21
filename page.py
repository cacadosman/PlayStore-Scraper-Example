from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MLPlayStorePage:
    def __init__(self, url):
        self.__url = url

        self.__driver = webdriver.Chrome(chrome_options=self.__chrome_options)
        self.__driver = webdriver.Firefox()

        self.__user_reviews_xpath =("/html[1]/body[1]/div[1]/div[4]/c-wiz[1]/div[1]" +
        "/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[position() >= {}]")
        self.__user_review_text_xpath = "./div/div[2]/div[2]/span[1]"
        self.__user_review_rating_xpath = "./div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[1]"

        self.__user_reviews_text_abs_xpath = ("/html[1]/body[1]/div[1]/div[4]/c-wiz[1]/div[1]" +
        "/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[position() >= {}]/div" +
        "/div[2]/div[2]/span[1]")

        self.__show_more_btn_xpath = ("/html[1]/body[1]/div[1]/div[4]/c-wiz[1]/div[1]/div[2]" +
        "/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")

    def __wait_until(self, ec, by, value):
        return WebDriverWait(self.__driver, 10).until(ec((by, value)))

    def execute_script(self, script):
        self.__driver.execute_script(script)

    def open(self, path = ""):
        self.__driver.get(self.__url + path)

    def get_user_reviews(self, start_index):
        return self.__wait_until(
            EC.presence_of_all_elements_located, 
            By.XPATH, 
            self.__user_reviews_text_abs_xpath.format(start_index)
        )

    def get_user_reviews_el(self, start_index):
        return self.__wait_until(
            EC.presence_of_all_elements_located, 
            By.XPATH, 
            self.__user_reviews_xpath.format(start_index)
        )

    def get_user_review_rating(self, user_review_el):
        return user_review_el.find_element_by_xpath(self.__user_review_rating_xpath).get_attribute("aria-label")

    def get_user_review_text(self, user_review_el):
        return user_review_el.find_element_by_xpath(self.__user_review_text_xpath).text

    def click_show_more(self):
        try:
            self.__driver.find_element_by_xpath(self.__show_more_btn_xpath).click()
        except:
            pass

    def scroll_to_bottom(self):
        self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def close(self):
        self.__driver.close()