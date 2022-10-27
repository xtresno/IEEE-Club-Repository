import requests
from datetime import datetime, timedelta
import json

today = datetime.today()

dateList = []

for day in range(0,50):
    date = today - timedelta(days=day)
    dateList.append(date.strftime("%Y-%m-%d"))


def requestImage(date_list):
    for date in date_list:
        url = f"https://api.nasa.gov/planetary/apod?api_key=RXnwrrQ6PVkBcL9umXseMxTIYvblFfGL1JN13oG3&date={date}"
        response = requests.request("GET", url)
        json_object = json.loads(response.text)
        image_url = json_object['url']
        try:
            sendToTelgram(image_url)
        except:
            print("skipping image, could not decode")
            continue

def sendToTelgram(message):
    url = f"https://api.telegram.org/bot5403320034:AAHn37GOwjdM7JwmSd7hhjGsqY4CF8U88KU/sendMessage?chat_id=-843458555&text={message}"
    response = requests.request("GET", url)
    if (response.status_code == 200):
        print(f"successfully sent message! response: {response}")

requestImage(dateList)

# we ran the program, got the result: but what the hell happened in between?