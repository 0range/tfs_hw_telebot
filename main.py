import telebot
from datetime import datetime

bot = telebot.TeleBot("854886760:AAHt7H2cwzYlAPbY6HHuhJ6W89T8IrUS264")
datafile = "data.txt"

@bot.message_handler(commands=['start'])
def handler_text(message):
    answer = "Привет. Я - бот, принимающий задания на лекциях финтех-школы. Начни с того, чтобы написать свои ФИО :)"
    sent = bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    with open(datafile, "a") as data:
        data.write(str(datetime.now()) + ";" + str(message.chat.id) + ";" + message.text + "\n")

bot.polling(none_stop=True, interval=1, timeout=60)
