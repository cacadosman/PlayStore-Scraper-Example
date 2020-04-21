from action import MLPlayStoreAction
import json
import time

action = MLPlayStoreAction()
total_reviews = 100
scroll_delay = 1
user_reviews = []

action.user_open_website()
user_reviews = action.user_get_all_reviews()

old_count = len(user_reviews)
while True:
    start_time = time.time()

    action.user_scroll_to_bottom()

    time.sleep(scroll_delay)
    action.user_click_show_more_button()
    new_user_reviews = action.user_get_all_reviews(old_count)

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

print("GET Last {} reviews...".format(total_reviews))
user_reviews = user_reviews[0:total_reviews]
print("Saving data to JSON format...")
data = {
    'reviews': user_reviews
}
f = open('mobile_legend_playstore_reviews.json', 'w')
f.write(json.dumps(data, indent = 4))
f.close()

print("DONE~")

