 #стандартные библиотеки
import logging

# side библиотеки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import User
#локальные модули
from handlers import greet_user, talk_to_me, bash_control, sensors, pwd_show, raspberry_temp, upload

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD
    }
}

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("ubuntu_sensors", sensors))
    dp.add_handler(CommandHandler("raspberry_temp", raspberry_temp))
    dp.add_handler(CommandHandler("pwd", pwd_show))
    dp.add_handler(MessageHandler(Filters.regex('^/get'), upload))
    dp.add_handler(MessageHandler(Filters.text, bash_control))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()