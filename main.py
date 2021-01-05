import COVID19Py
import telebot
from telebot import types
from threading import Thread
import Key_python
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(Key_python.Telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_about = types.InlineKeyboardButton(text='Обо мне ', callback_data='about')
    markup_inline.add(item_about)
    bot.send_message(message.chat.id,
                     'Привет!\nВведи страну где ты живешь\nЧтобы узнать больше нажми кнопку!Введи страну где ты живешь\n',
                     reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def hello(call):
    if call.data == "about":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_world = types.KeyboardButton('world')
        markup_reply.add(item_world)
        bot.send_message(call.message.chat.id,
                         '<b>Я кабот!</b>\nМогу рассказать тебе про статистику коронавируса🦠\n<u>Для этого просто напиши страну, про которую хочешь узнать</u>🇷🇺\nИли нажми на кнопку ⬇️',
                         reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'world':
        location = covid19.getLatest()

        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == 'сша':
        location = covid19.getLocationByCountryCode("US")
        final_message =  (f"Привет{location[0]['latest']['confirmed']}Пока{location[0]['latest']['deaths']}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode("RU")
        final_message = (f"<b>Данные по России</b>\n<u>Заболевших: </u>{location[0]['latest']['confirmed']}\n<u>Погибли: </u>{location[0]['latest']['deaths']}")

        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == 'италия':
        location = covid19.getLocationByCountryCode("IT")
        final_message = (f"<b>Данные по России</b>\n<u>Заболевших: </u>{location[0]['latest']['confirmed']}\n<u>Погибли: </u>{location[0]['latest']['deaths']}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop = True)

