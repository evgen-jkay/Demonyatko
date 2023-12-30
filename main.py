# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привіт":
        bot.send_message(message.from_user.id, "Привіт, а я ще в розробці, тому багато не можу =(")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "А тут буде допомога. Напиши мені Привіт")
    else:
        bot.send_message(message.from_user.id, "Я тебе не розумію. Напиши /help.")


bot.polling(none_stop=True, interval=0)
