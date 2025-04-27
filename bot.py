
import os
import random
import telebot

TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_USERNAME = 'vinksyu_art'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not is_subscribed(user_id):
        bot.send_message(message.chat.id, "Чтобы получать карты дня, подпишитесь на канал @vinksyu_art.")
    else:
        bot.send_message(message.chat.id, "Привет! Нажми /card чтобы получить свою карту дня.")

@bot.message_handler(commands=['card'])
def send_card(message):
    user_id = message.from_user.id
    if not is_subscribed(user_id):
        bot.send_message(message.chat.id, "Пожалуйста, подпишитесь на канал @vinksyu_art для получения карт.")
        return
    card_path = random.choice(os.listdir('cards'))
    with open(f'cards/{card_path}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="С теплом и верой в твой свет,\nКсения Виноградова ✨")

def is_subscribed(user_id):
    try:
        member = bot.get_chat_member('@' + CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'creator', 'administrator']
    except Exception:
        return False

bot.polling(non_stop=True)
