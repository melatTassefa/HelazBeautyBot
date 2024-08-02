import requests
import time
from bs4 import BeautifulSoup
import requests
url = 'https://helazbeauty.com/collections'
name = []
img = []
src = requests.get(url)
# src.raise_for_status()

soup = BeautifulSoup(src.text,'html.parser')
#print(soup)
collections = soup.find('ul', class_="collection-list").find_all('li')
#print(len(collections))
for col in collections:
    nm = col.find('a').h2.get_text(strip=True)
    imdiv1 = col.find('a').find('div', class_="card--stretch card-colored color-background-1")
    imdiv2 = imdiv1.find('div', class_="media media--square media--hover-effect overflow-hidden")
    img.append(imdiv2.find("img")["src"]) if col.find("img") else "Image URL not found"
    name.append(nm)
# print(name)
# print(img)
#Set up bot and channel information
bot_token = "6214833762:AAFQs2wI6A2bv5nXT631qgv4ftFdOjwQsBo"
channel_id = "-1001828159783"

# Define function to send message to Telegram channel
def send_message(message):
    bot_token = "6214833762:AAFQs2wI6A2bv5nXT631qgv4ftFdOjwQsBo"
    channel_id = "-1001828159783"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": channel_id, "text": message}
    requests.post(url, json=payload)

# Define function to send image to Telegram channel
def send_image(image_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    params = {
        'chat_id': channel_id,
        'photo':"https:" + image_path,
    }
    requests.get(url, params=params)

# Define function to send text and image to Telegram channel open(image_path, "rb")
def send_data(text_list, image_list):
    for i in range(len(text_list)):
        send_message(text_list[i])
        send_image(image_list[i])
        time.sleep(30)
# Send data every 30 seconds until the data ends
send_data(name, img)
