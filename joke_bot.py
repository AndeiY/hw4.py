import telebot
import time
bot = telebot.TeleBot('5233184232:AAGSdw71rdoeWW1gp_RQx3MaJlK353Pvoq4')
CHANNEL_NAME = '@адрес_твоего_канала'
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
