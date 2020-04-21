from action import MLPlayStoreAction
import pandas as pd
import json
import time

action = MLPlayStoreAction()
total_reviews = 10000
scroll_delay = 0.1
user_reviews = []

action.user_open_website()
user_reviews = action.user_get_all_reviews_with_rating()

old_count = len(user_reviews)
while True:
    start_time = time.time()

    action.user_scroll_to_bottom()
    time.sleep(scroll_delay)
    action.user_click_show_more_button()
    new_user_reviews = action.user_get_all_reviews_with_rating(old_count)
    time.sleep(scroll_delay)
    action.user_click_show_more_button()

    end_time = time.time()
    new_count = old_count + len(new_user_reviews)
    print("Scraping {} reviews, TIME: {} sec".format(new_count, end_time - start_time))
    
    if (new_count == old_count):
        break

    user_reviews += new_user_reviews
    if (new_count >= total_reviews):
        break

    old_count = new_count

action.user_close_website()

print("GET First {} reviews...".format(total_reviews))
user_reviews = user_reviews[0:total_reviews]

print("Saving data to JSON format...")
f = open('mobile_legend_playstore_reviews.json', 'w')
f.write(json.dumps(user_reviews, indent = 4))
f.close()

print("Saving data to EXCEL format...")
pd.read_json("mobile_legend_playstore_reviews.json").to_excel("mobile_legend_playstore_reviews.xlsx")

print("DONE~")

