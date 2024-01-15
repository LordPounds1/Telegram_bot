import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6519856683:AAHy5KDNzXzSF_Fj83a7SzNZbzoP9eYKjOA')

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Перейти на сайт")
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./da.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'Привет' ,reply_markup=markup)
    #bot.send_audio(message.chat.id, file.mp3, reply_markup=markup)
    #bot.send_vidio(message.chat.id, file.mp4, reply_markup=markup)
    bot.register_next_step_handler(message, on_click)\

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id,'web_site')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')



@bot.message_handler(commands=['site','website'])

def site(message):
    webbrowser.open('https://www.youtube.com')



@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, 'Help information')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url="https://www.youtube.com")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото',callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст',callback_data='edit')
    markup.row(btn2,btn3)
    bot.reply_to(message,'Зачет',reply_markup=markup)




bot.polling(none_stop=True)