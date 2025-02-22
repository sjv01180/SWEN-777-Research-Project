from google_play_scraper import Sort, reviews_all
import csv, json

result = reviews_all(
    'com.google.android.apps.healthdata',
    sleep_milliseconds=0,
    lang='en',
    country='us',
    sort=Sort.RATING
)
# /print(result[0])
with open("HealthConnectReviews.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['reviewId', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'appVersion'])
    for i in result:
        if i['score'] <= 2:
            review = [i['reviewId'], i['content'], i['score'], i['thumbsUpCount'], i['reviewCreatedVersion'], i['at'], i['appVersion']]
            writer.writerows([review])
file.close()        
