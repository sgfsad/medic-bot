
import os
import telebot
from boto.s3.connection import S3Connection
token = S3Connection(os.environ['token'])
bot = telebot.TeleBot(token)

bot.send_message(868719453, "test")
