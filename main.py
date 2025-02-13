import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Get the token from Render environment variables
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome to the Render-hosted bot!")

@bot.message_handler(commands=['order'])
def take_order(message):
    bot.send_message(message.chat.id, "Enter your order details:")

@bot.message_handler(commands=['status'])
def order_status(message):
    bot.send_message(message.chat.id, "Your order is being processed!")

bot.polling()
