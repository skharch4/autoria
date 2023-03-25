"""

import requests

BASE_URL = "https://developers.ria.com/auto/search"
API_KEY = "ia2nFHAfbae8MKBRKHyROJcqnK7v9O7LBszwPCwy"

#https://developers.ria.com/auto/search?api_key=YOUR_API_KEY&PARAMETERS
#url= BASE_URL + "?api_key=" + API_KEY + "&year=2016&brand=6"

url= BASE_URL + "?api_key=" + API_KEY + "&s_yers[0]=2010&po_yers[0]=2017&marka_id[0]=75&model_id[0]=3094"
response = requests.get(url).json()
print(response)

needid=['main'],['ids']
print(f" Needed IDs here: {needid}")
#url= BASE_URL + "?api_key=" + API_KEY + "&year=2016&marka_id=6"
"""
#ID = response[""]
import requests
from bs4 import BeautifulSoup
import telegram
#ёfrom telegram.ext import CommandHandler, MessageHandler, Filters, Updater
url = "https://developers.ria.com/auto/used/autos/advertisementId?user_id=12307491&api_key=ia2nFHAfbae8MKBRKHyROJcqnK7v9O7LBszwPCwy"
response = requests.get(url).json()
print(response)
"""
"""

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Autobot! Type /search followed by a car model to find matching listings on autoria.com")

# Define a function to handle the /search command
def search(update, context):
    query = context.args[0]
    url = f'https://auto.ria.com/search/?category_id=1&marka_id=223&model_id=0&city=0&price_ot=0&price_do=0&currency=1&state=0&newauto=&fuelRatesId=0&gearbox=&year_ot=&year_do=&mileage=0&doors=&seats=&engineVolumeFrom=&engineVolumeTo=&powerFrom=&powerTo=&exchange=&damage=&custom=0&top=1&saledParam=0&search_top_actual=1&scrollToAuto=1263'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B08C390',
    }
    params = {
        'indexName': 'auto',
        'section': 'auto',
        'category_id': 1,
        'marka_id': 75,
        'lang_id': 2,
        'output_type': 3,
        'top': 1,
        'order': 'date_added',
        'page': 0,
        'limit': 10,
        'model_id': 59651,
        'year[0]': 0,
        'price_usd[0]': 0,
        'price_usd[1]': 0,
        'currency': 1,
        'state': 0,
        'city': 0,
        'damage': 0,
    }
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    cars = []
    for item in soup.find_all('section', {'class': 'ticket-item'}):
        title = item.find('div', {'class': 'head-ticket'}).text
        price = item.find('span', {'class': 'price-ticket'}).text
        cars.append(f"{title}\nPrice: {price}")
    if not cars:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No results found for that query. Please try again.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="\n\n".join(cars))

# Define the main function to start the bot
def main():
    # Create a Telegram bot object with your API key
    bot = telegram.Bot(token='YOUR_API_KEY')

    # Create an Updater object to receive messages from Telegram
    updater = Updater(token='YOUR_API_KEY', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for the /start and /search commands
    start_handler = CommandHandler('start', start)
    search_handler = CommandHandler('search', search)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search)



#open('api_key', 'r').read()

#list.sunset Sunset time, Unix, UTC
#list.temp
#list.temp.day Day temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
#print($temperature);
#json