import telebot 
import os 
import random 


bot = telebot.TeleBot("TOKEN")
@bot.message_handler(commands=["mem"])
def start(message: True):
    with open('images/images.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["random_meme"])
def send_random_meme(message: True):
    randomlist = (os.listdir('images'))
    randomimage = random.choice(randomlist)
    with open(f'images/{randomimage}', 'rb') as f:
        bot.send_photo(message.chat.id, f)        
bot.polling()  


#(os.listdir('images'))
