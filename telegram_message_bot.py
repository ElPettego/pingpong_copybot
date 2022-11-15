import logging
from telegram.ext import Updater
import time
import telegram

class TelegramBot:

    def __init__(self, chat_id, bot_token):
        self.chat_id = chat_id
        self.bot_token = bot_token
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logger = logging.getLogger(__name__)   
                
    def emit(self, mex):

        updater = Updater(self.bot_token, use_context=True)
        dp = updater.dispatcher
        bot = telegram.Bot(token=self.bot_token)


        status = bot.send_message(chat_id=self.chat_id, text=mex, parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)
        # time.sleep(0.2)
        # print(status)
        updater.start_polling()
        # time.sleep(0.2)
        updater.stop() 
        
    def send_file(self, path_to_file):
        updater = Updater(self.bot_token, use_context=True)
        dp = updater.dispatcher
        bot = telegram.Bot(token=self.bot_token)
        status = bot.send_document(chat_id=self.chat_id, 
                                   document=open(path_to_file, 'rb'),
                                   filename=path_to_file,
                                   parse_mode=telegram.ParseMode.HTML)
        time.sleep(0.2)
        print(f'INVIANDO FILE A {self.chat_id}.')
        updater.start_polling()
        time.sleep(0.2)
        updater.stop()
