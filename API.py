import os
from telebot import *
from _token import TOK
from core import speech_to_text

bot = telebot.TeleBot(TOK)

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    file_path = bot.get_file(message.voice.file_id).file_path
    downloaded_file = bot.download_file(file_path)

    bot.reply_to(message, speech_to_text(downloaded_file))


bot.polling()