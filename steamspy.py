# -*- coding: utf-8 -*-
import bs4
import requests
import telebot
import re
token=''
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text'])

def handle_text(message):
    try:
        try:
            s = requests.get('http://steamcommunity.com/id/')  // steam_id
            b = bs4.BeautifulSoup(s.text, "html.parser");
        except:
            print("TimeOut")
        if message.text == "steam":
            bot.send_message(message.chat.id, b.find('div', {'class':'profile_in_game_name'}).string)
    except:
        bot.send_message(message.chat.id, "В сети")




bot.polling(none_stop=True, interval = 0)