from bs4 import BeautifulSoup
import requests
from telegram.ext import ConversationHandler
from utils import get_keyboard
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')  # вывод сообщения в консоль, когда нажимают /start
    bot.message.reply_text('Здравствуйте, {}! я бот, а ты иди нахуй чмошник обрыганный! \n'
                           'Я пока не умею разговаривать, но ебало тебе быстро снесу'.format(
        bot.message.chat.first_name), reply_markup=get_keyboard())
    print(bot.message)  # ?


def get_anecdote(bot, update):
    receive = requests.get('http://anekdotme.ru/random')
    page = BeautifulSoup(receive.text, "html.parser")
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    bot.message.reply_text(page)


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def get_contact(bot, update):
    print(bot.message.contact)
    bot.message.reply_text('{}, мы получили ваш номер телефона'.format(bot.message.chat.first_name))


def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('{}, мы получили ваше местоположение'.format(bot.message.chat.first_name))


def anketa_start(bot, update):
    bot.message.reply_text('Как вас зовут?', parse_mode='Markdown')
    return "user_name"


def anketa_get_name(bot, update):
    update.user_data['name'] = bot.message.text  # временно сохраняем ответ
    bot.message.reply_text("Сколько вам лет?")  # задаем вопрос
    return "user_age"  # ключ для определния след. шага


def anketa_get_age(bot, update):
    update.user_data['age'] = bot.message.text  # временно сохраняем ответ
    reply_keyboard = [["1", "2", "3", "4", "5"]]  # создаем клаву
    bot.message.reply_text(
        'Оцените статью от 1 до 5',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True,
            one_time_keyboard=True))  # one_time_keyboard=True при нажатии клавиатура исчезает
    return "evalution"  # ключ для определения след. шага


def anketa_get_evalution(bot, update):
    update.user_data['evalution'] = bot.message.text
    reply_keyboard = [["Пропустить"]]
    bot.message.reply_text("Напишите отзыв или нажмите кнопку пропустить этот шаг.",
                           reply_markup=ReplyKeyboardMarkup(
                               reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return "comment"


def anketa_comment(bot, update):
    update.user_data['comment'] = bot.message.text
    text = """Результат опроса:
    <b>Имя:</b> {name}
    <b>Возраст:</b> {age}
    <b>Оценка:</b> {evalution}
    <b>Комментарий:</b> {comment}
    """.format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text("Спасибо вам за комментарий!", reply_markup=get_keyboard())
    return ConversationHandler.END


def anketa_exit_comment(bot, update):
    text = """Результат опроса:
    <b>Имя:</b> {name}
    <b>Возраст:</b> {age}
    <b>Оценка:</b> {evalution}""".format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text("Спасибо ^^", reply_markup=get_keyboard())


def dontknow(bot, update):
    bot.message.reply_text("Я вас не понимаю, выберите оценку на клавиатуре!")


