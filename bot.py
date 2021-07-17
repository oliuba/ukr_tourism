"""This is the module with a Telegram bot for traveling."""

import telebot
from main_travel import main_travel
from search_url import info
from conf import tok

bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Initial message
    """
    bot.reply_to(message, "Привіт! Я український бот-мадрівник!")


@bot.message_handler(commands=['travel'])
def handle_travel(message):
    """
    Give a place for traveling and info about it.
    """
    place = main_travel()
    url = info(place)
    reply = f'Вітаємо! Твій результат - {place}.\n\
Додаткову інформацію про це місце знайдеш тут: {url}\nГарної мандрівки!'
    bot.reply_to(message, reply)


@bot.message_handler(commands=['help'])
def handle_help(message):
    """
    Give help to user.
    """
    help_message = 'Доступні команди:\n\
/start - почати роботу з ботом;\n\
/travel - отримати місце для мандрівки.'
    bot.reply_to(message, help_message)


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    """
    Send messages to the bot.
    """
    bot.reply_to(message, 'На жаль, я не розумію твого повідомлення.')


bot.polling()
