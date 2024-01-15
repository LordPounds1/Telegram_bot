import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6519856683:AAHy5KDNzXzSF_Fj83a7SzNZbzoP9eYKjOA')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,'Введите сумму')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Дай цифры жи есть')
        bot.register_next_step_handler(message,summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/CNY', callback_data='usd/cny')
        btn5 = types.InlineKeyboardButton('RUB/INR',callback_data='rub/inr')
        btn6 = types.InlineKeyboardButton('INR/RUB',callback_data='inr/rub')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id,'Выбери пару валют',reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Еблан? введи число больше 0')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount,values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)} Впиши еще')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введи через /')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)} Впиши еще')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Еблан? впиши нормально')
        bot.register_next_step_handler(message, my_currency)

bot.polling(none_stop=True)