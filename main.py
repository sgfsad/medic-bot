
import telebot
import constants
bot = telebot.TeleBot(constants.token)

bot.send_message(868719453, "test")
