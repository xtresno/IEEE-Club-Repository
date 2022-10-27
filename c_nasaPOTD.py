import requests
from datetime import datetime, timedelta
import json

# we declare a variable today and initalize the current date to it using the today() function
today = datetime.today()

# define an empty list; we will add on to it later.
dateList = []

# create a for loop with variable called "day" and make the function limited to a range from 0 to 51
# start(exclusive), stop(exclusive)

# The range(n) is exclusive, so it doesn't include the last number in the result.
# however, it does include the first parameter and exclude the second.

for day in range(0,51):

    # A timedelta object represents a duration, the difference between two dates or times.
    date = today - timedelta(days=day)

    # The strftime() function is used to convert date and time objects to their string representation.
    dateList.append(date.strftime("%Y-%m-%d"))


# create a function called "requestImage" and pass in a parameter called "date_list"
def requestImage(date_list):
    # then, for every date in the date list, we want to request the nasa picture of the day DATE, which will respond with the
    # nasa POTD's corresponding date.
    for date in date_list:
        url = f"https://api.nasa.gov/planetary/apod?api_key=RXnwrrQ6PVkBcL9umXseMxTIYvblFfGL1JN13oG3&date={date}"

        # gets the entire response of the request as well as the status code. (did it succeed or not)
        response = requests.request("GET", url)
        # print(response) 
        # should respond with 200! try to change the url so it will result in an error as well as the 400 status code. ;)

        # define another variable that uses the json.loads method in order to convert the STRING response from the text into JSON format.
        json_object = json.loads(response.text)

        # for this, we need to look at the json response of the request.
        # in doing so, we can declare a new variable called "image_url" and then access the url by INDEXING the JSON response.
        image_url = json_object['url']
        # error handling, because we dont know if the response of the request will be an image or invalid.
        try:
            sendToTelgram(image_url)
        except:
            print("skipping image, could not decode")
            continue


# define another function called "sendToTelegram" with a parameter called "message"
def sendToTelgram(message):
    url = f"https://api.telegram.org/bot5403320034:AAHn37GOwjdM7JwmSd7hhjGsqY4CF8U88KU/sendMessage?chat_id=-843458555&text={message}"
    response = requests.request("GET", url)
    # if the request is successful, print that it was successful
    if (response.status_code == 200):
        print(f"successfully sent message! response: {response}")

# call the function and pass in the datelist array.
requestImage(dateList)

