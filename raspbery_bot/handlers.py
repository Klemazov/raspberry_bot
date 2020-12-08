import os 
import subprocess

from telegram import ReplyKeyboardMarkup
from keyboard import keyboard
from utils import BashControls

def greet_user(update, context):
    print('Вызван /start')
    user_id = update.message.from_user['username']
    greet_keyboard = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(f'Вызван /start {user_id}', reply_markup = greet_keyboard)

def talk_to_me(update, context):
    text = update.message.text
    print (text)
    update.message.reply_text(text)

def bash_control(update, context):
    command = update.message.text
    if 'cd' in command:
        os.chdir(command[3:])
        update.message.reply_text(os.popen('pwd').read())
    else:
        result = os.popen(command)
        update.message.reply_text(result.read())
    
def sensors(update, context):
    print('Вызван /temperature')
    sensors = 'sensors'
    command = os.popen(sensors)
    update.message.reply_text(command.read())

def raspberry_temp(update, context):
    temperature = 'vcgencmd measure_temp'
    command = os.popen(temperature)
    update.message.reply_text(command.read())


def pwd_show (update, context):
    command = os.popen('pwd')
    update.message.reply_text(command.read())




    