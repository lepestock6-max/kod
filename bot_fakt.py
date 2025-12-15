import telebot
import os 
import random 


bot = telebot.TeleBot("8498699409:AAGjjrx0F1IYzp9VPXFupXIxFF54fxQScGA")
@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    text = "привет я помогу тебе в твоей нелёгкой работе, для помощи в командах напиши /help"
    bot.send_message(message.chat.id , text)

@bot.message_handler(commands=["help"])
def start(message: telebot.types.Message):
    text = "Напишите /random_fakt для того чтобы у вас на экране появился случайный интересный факт \n Напишите /musor чтобы узнать куда нужно кидать пластковый мусор"
    bot.send_message(message.chat.id , text)    

@bot.message_handler(commands=["random_fakt"])
def send_random_meme(message: True):
    randomlist = (os.listdir('images'))
    randomimage = random.choice(randomlist)
    with open(f'images/{randomimage}', 'rb') as f:
        bot.send_photo(message.chat.id, f)        

@bot.message_handler(commands=["musor"])
def send_random_meme(message: True):
    randomlist = (os.listdir('images1'))
    randomimage = random.choice(randomlist)
    with open(f'images1/{randomimage}', 'rb') as f:
        bot.send_photo(message.chat.id, f)          
        
              

bot.polling()
