import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# API কী এবং URL
API_KEY = "7322638031:AAHVOAEuQCYZWrTe96RTzSXz_VSuI8Xaogc"
API_URL = "https://advego.com/user/password/#tab-user-keyapi-hash"

def fetch_data_from_website():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

def start(update: Update, context: CallbackContext) -> None:
    data = fetch_data_from_website()
    if "error" in data:
        update.message.reply_text("Error fetching data from website.")
    else:
        update.message.reply_text(f"Data from website: {data}")

def main():
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
