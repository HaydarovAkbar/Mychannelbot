"""
dasturchi: Haydarov Akbar
sana: 11/05/2021
"""
from Algorithm_channel_bot import *
from telegram.ext import Updater,MessageHandler,CommandHandler,Filters,CallbackQueryHandler

Token = "" # Your token

updater = Updater(token=Token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start",start)
text_handler = MessageHandler(Filters.text,main)
file_handler = MessageHandler(Filters.document, document)
photo_handler = MessageHandler(Filters.photo, photo)
voice_handler = MessageHandler(Filters.voice, voice)
call_handler = CallbackQueryHandler(call_back)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(file_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(voice_handler)
dispatcher.add_handler(call_handler)

updater.start_polling()