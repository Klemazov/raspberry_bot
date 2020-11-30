import os 

from telegram import ReplyKeyboardMarkup
from keyboard import keyboard


def greet_user(update, context):
    print('Вызван /start')
    greet_keyboard = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Вызван /start', reply_markup = greet_keyboard)

def talk_to_me(update, context):
    text = update.message.text
    print (text)
    update.message.reply_text(text)

def bash_controls(update, context):
    print('можете использовать bash команды')
    command = update.message.text
    try:
        command = os.popen(command) # выполнение bash команды
        update.message.reply_text(command.read())
    except Exception:
        print('Что-то пошло не так')
    