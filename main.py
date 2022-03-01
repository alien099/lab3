import telebot
import random
from telebot import types

f = open('data/all.txt', 'r', encoding='UTF-8')
books = f.read().split('\n')
f.close()

f = open('data/fantasy.txt', 'r', encoding='UTF-8')
fantasy = f.read().split('\n')
f.close()


f = open('data/detective.txt', 'r', encoding='UTF-8')
detective = f.read().split('\n')
f.close()

bot = telebot.TeleBot('5280932131:AAELkJM_n0-ndTQ-bvmrlCThjDsgcGdYG7A')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я ПайТон. Я могу помочь тебе с выбором книг для чтения.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "🔙" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Жанры")
        btn2 = types.KeyboardButton("Поиск по названию или автору")
        btn3 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Жанры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Детектив")
        btn2 = types.KeyboardButton("Фантастика")
        btn3 = types.KeyboardButton("Приключения")
        btn4 = types.KeyboardButton("Роман")
        btn5 = types.KeyboardButton("Юмор")
        back = types.KeyboardButton("🔙")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="Открываю жанры", reply_markup=markup)

    elif ms_text == "Фантастика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Фэнтези")
        btn2 = types.KeyboardButton("Научная фантастика")
        back = types.KeyboardButton("🔙")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Перехожу в жанр фантастики", reply_markup=markup)

    elif ms_text == "Фэнтези":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, random.choice(fantasy))

    elif ms_text == "Детектив":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, random.choice(detective))

    elif ms_text == "Юмор" or ms_text == "Фольклор" or ms_text == "Роман" or ms_text == "Приключения":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Поиск по названию или автору":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Управление":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "/help" or ms_text == "Помощь":
        bot.send_message(chat_id, "Автор: Белоцерковец Алина")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напиши автору", url="https://t.me/Litareae")
        key1.add(btn1)
        img = open('Фото.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:

        bot.send_message(chat_id, text="Я тебя слышу! Твое сообщение: " + ms_text)


bot.polling(none_stop=True, interval=0)

print()