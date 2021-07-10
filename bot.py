from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TG_TOKEN, TG_API_URL


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?') #вывод сообщения в консоль, когда нажимают /start
    bot.message.reply_text('Здравствуйте, {}! я бот, а ты иди нахуй чмошник обрыганный! \n'
                            'Я пока не умею разговаривать, но ебало тебе быстро снесу'.format(bot.message.chat.first_name))
    print(bot.message)


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms)) # обработчик команды
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling() # проверяет о наличие сообщений в ТГ
    my_bot.idle() # бот будет работать, пока его не остановят

# вызываем функцию запсука бота main
main()