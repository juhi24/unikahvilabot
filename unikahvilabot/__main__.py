# coding: utf-8
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from unikahvilabot import config, unicafe
import logging

logging.basicConfig(format='{levelname:8s} {name}: {message}', style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hello! Are you hungry?')


def halp(bot, update):
    update.message.reply_text('Help!')


def menu(bot, update):
    restaurants = (10, 11)
    for r in restaurants:
        text = unicafe.restaurant_name(r) + '\n' + unicafe.menu(r)
        update.message.reply_text(text)

def error(bot, update, error):
    '''error handling: log errors'''
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    conf = config.initialize_config()
    token = conf['general']['token']
    if len(token)<1:
        raise Exception('Token not set.')
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', halp))
    dp.add_handler(CommandHandler('menu', menu))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    # execute only if run as a script
    main()



loc = [None,
       'Latin Market Metsätalo',
       'Olivia',
       None, 
       'Päärakennus',
       'Cafe Portaali',
       'Topelias',
       'Ylioppilasaukio',
       'Chemicum',          # 10
       'Exactum',
       'Physicum',
       'Meilahti']
