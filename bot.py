import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from settings import TG_TOKEN
from telebot import apihelper
from handlers import *

apihelper.proxy = {"https": "129.226.144.129:19000"}

def main():
    my_bot = Updater(TG_TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик команды
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Анекдот'), get_anecdote))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))
    my_bot.dispatcher.add_handler(ConversationHandler(entry_points=[MessageHandler(Filters.regex('Заполнить анкету'), anketa_start)],
                                                      states={
                                                          "user_name": [MessageHandler(Filters.text, anketa_get_name)],
                                                          "user_age": [MessageHandler(Filters.text, anketa_get_age)],
                                                          "evalution": [MessageHandler(Filters.regex('1|2|3|4|5'), anketa_get_evalution)],
                                                          "comment": [MessageHandler(Filters.regex('Пропустить'), anketa_exit_comment),
                                                                      MessageHandler(Filters.text, anketa_comment)]
                                                      },
                                                      fallbacks=[MessageHandler(
                                                          Filters.text | Filters.video | Filters.photo | Filters.document, dontknow)]
                                                      )
                                  )
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()  # проверяет о наличие сообщений в ТГ
    my_bot.idle()  # бот будет работать, пока его не остановят


# вызываем функцию запсука бота main
if __name__ == "__main__":
    main()
