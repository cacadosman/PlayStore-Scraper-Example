from page import MLPlayStorePage

class MLPlayStoreAction:
    def __init__(self):
        self.__base_url = 'https://play.google.com/store/apps/details?id=com.mobile.legends&hl=en_GB&showAllReviews=true'
        self.__page = MLPlayStorePage(self.__base_url)
    
    def user_open_website(self):
        self.__page.open()
    
    def user_get_all_reviews(self, start_index = 0):
        user_reviews_el = self.__page.get_user_reviews(start_index)
        return [el.text for el in user_reviews_el]
    
    def user_scroll_to_bottom(self):
        self.__page.scroll_to_bottom()

    def user_click_show_more_button(self):
        self.__page.click_show_more()
    
    def user_close_website(self):
        self.__page.close()