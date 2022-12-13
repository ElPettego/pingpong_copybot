from telegram.ext import Updater
import time
import telegram

class TelegramBot:
    def __init__(self, chat_id, bot_token):
        self.chat_id = chat_id
        self.bot_token = bot_token
        self.updater = Updater(self.bot_token, use_context=True)
        dp = self.updater.dispatcher
        self.bot = telegram.Bot(token=self.bot_token)

    def emit(self, mex):
        status = self.bot.send_message(chat_id=self.chat_id, text=mex, parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)
        self.updater.start_polling()
        # time.sleep(0.2)
        self.updater.stop() 
        
    def send_file(self, path_to_file):
        status = self.bot.send_document(chat_id=self.chat_id, 
                                   document=open(path_to_file, 'rb'),
                                   filename=path_to_file,
                                   parse_mode=telegram.ParseMode.HTML)
        time.sleep(0.2)
        print(f'INVIANDO FILE A {self.chat_id}.')
        self.updater.start_polling()
        time.sleep(0.2)
        self.updater.stop()
