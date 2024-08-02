import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import time
from bs4 import BeautifulSoup
import requests
def firstPost():
    img1 = []
    url="https://helazbeauty.com/"
    src = requests.get(url)
    soup = BeautifulSoup(src.text,'html.parser')
    header = soup.find("h1", class_="header__heading").find("a")
    collections1 = soup.find("div", class_="collage-content card-colored color-background-1").find("div", class_ = "collage-card__image-wrapper media media--transparent media--hover-effect")
    img1.append(header.find("img")["src"]) if header.find("img") else "Image URL not found"
    # print(collections1)
    img1.append(collections1.find("img")["src"]) if collections1.find("img") else "Image URL not found"
    print(img1)
# firstPost()

def createButton():
    keyboard = [[InlineKeyboardButton("Button 1", callback_data='function1'), InlineKeyboardButton("Button 2", callback_data='function2')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

# Send the message with the inline keyboard to your Telegram channel
    bot = telegram.Bot(token='6649016175:AAEfHvRVRGlgu6HfgInzi-u4NaCpNOIn05U')
    bot.send_message(chat_id='-1001828159783', text='Choose an option:', reply_markup=reply_markup)

createButton()