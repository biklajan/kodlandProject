import config
import telebot
import random
from telebot.util import extract_arguments


bot = telebot.TeleBot(config.token)

quotes = {
    1: "Работа не волк, никто не волк, только волк - волк",
    2: "Если ты первый, ты - первый",
    3: "Запомни, одна ошибка и ты ошибся",
}

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


    def info(self):
        info_text = (f"Марка: {self.brand}\nЦвет: {self.color}")
        return info_text

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['цитата'])
def send_welcome(message):
    number = random.randint(1, len(quotes))
    bot.reply_to(message, quotes[number])


@bot.message_handler(commands=['car'])
def send_welcome(message):
    full_text = extract_arguments(message.text)
    parts = full_text.split(' ', 1)
    color = parts[0]
    brand = parts[1]
    car = Car(color, brand)
    car_info = car.info()
    bot.reply_to(message, car_info)


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()