#!/usr/bin/env python3

# bot configuration
from HSFL_LNN import bot_config

# Telegram-API
import telegram.ext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

# Libraries
import sys, os, threading, logging
import datetime, time
import sqlite3

# Internal
from HSFL_LNN.SQLiteConnection import SQLiteConnection

# Job-Queue
import pickle
from threading import Event

<<<<<<< HEAD
MODUS = range(1)
=======
# Pytest
import pytest
>>>>>>> 8a0b9dd6b875ca845c21e438dd4775ecb7934592

def test_funcfast():
    time.sleep(0.1)

def test_funcslow():
    time.sleep(0.3)

MODUS = range(1)

### MENUE PANEL ###
keyboard2 =	[['Grades', 'News', 'Grades OFF', 'News OFF', 'Abort']
		]
markup2 = ReplyKeyboardMarkup(keyboard2)

def start(update, context):
    with SQLiteConnection('hsfl_lnn.db') as db:
        try:
            user_id = update.message.from_user.id
        except (NameError, AttributeError):
            try:
                user_id = update.inline_query.from_user.id
            except (NameError, AttributeError):
                try:
                    user_id = update.chosen_inline_result.from_user.id
                except (NameError, AttributeError):
                    try:
                        user_id = update.callback_query.from_user.id
                    except (NameError, AttributeError):
                        return ConversationHandler.END
        if user_id not in bot_config.BOT_ADMINS:
            update.message.reply_text('Hello %s %s.This is a private Bot.Your ChatID: "%s" has been blocked.' % (update.message.from_user.first_name, update.message.from_user.last_name, update.message.chat_id))
            return ConversationHandler.END
        else:
            update.message.reply_text('Welcome to the HSFL - LNN BOT', reply_markup=markup2)
            return MODUS

def crawl_news_job(update: telegram.Update, context: telegram.ext.CallbackContext):
    """ Send notification to user """
    update.message.reply_text('Activate News Job', reply_markup=markup2)
    context.job_queue.run_repeating(crawl_news, interval=300, first=0)

def crawl_news(context: telegram.ext.CallbackContext):
    os.system("scrapy crawl hsfl_latestnewsnotify")
    send_news(context)

def send_news(context: telegram.ext.CallbackContext):
    with SQLiteConnection('hsfl_lnn.db') as db:
        news = db.query('SELECT * FROM latestNews WHERE timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
        for news_card in news:
            text = '<a href="' + str(news_card[4]) + '">' + str(news_card[1]) + '</a>\n' + str(news_card[3])
            context.bot.send_message(chat_id="-1001183748964", text=text, parse_mode=ParseMode.HTML)

def crawl_grades(update, context: telegram.ext.CallbackContext):
    os.system("scrapy crawl hsfl_latestgradesnotify")

def crawl_grades_job(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.job_queue.run_repeating(crawl_grades, interval=60, first=0)

def send_grades(update, context):
    ## Wirtschaftsinformatik
    with SQLiteConnection('hsfl_lnn.db') as db:
        wi = db.query('SELECT * FROM latestGrades WHERE study_course_id = "wi" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in wi:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001448706085", text=str(text), parse_mode=ParseMode.HTML)

    ## Betriebswirtschaft
    with SQLiteConnection('hsfl_lnn.db') as db:
        bw = db.query('SELECT * FROM latestGrades WHERE study_course_id = "bw" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in bw:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001151194560", text=str(text), parse_mode=ParseMode.HTML)

    ## Energiewissenschaft
    #with SQLiteConnection('hsfl_lnn.db') as db:
    #    ew = db.query('SELECT * FROM latestGrades WHERE study_course_id = "ew" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    #for exam in ew:
    #    text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
    #    # channels and supergroups have a -100 prefix
    #    context.bot.send_message(chat_id="-1001452978901", text=str(text), parse_mode=ParseMode.HTML)

    ## Angewandte Informatik
    #with SQLiteConnection('hsfl_lnn.db') as db:
    #    ai = db.query('SELECT * FROM latestGrades WHERE study_course_id = "ai" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    #for exam in ai:
    #    text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
    #    # channels and supergroups have a -100 prefix
    #    context.bot.send_message(chat_id="-1001260953220", text=str(text), parse_mode=ParseMode.HTML)

    ## Maschinenbau
    with SQLiteConnection('hsfl_lnn.db') as db:
        mb = db.query('SELECT * FROM latestGrades WHERE study_course_id = "mb" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in mb:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001463785161", text=str(text), parse_mode=ParseMode.HTML)

    ## Bio- Verfahrenstechnik
    #with SQLiteConnection('hsfl_lnn.db') as db:
    #    bvt = db.query('SELECT * FROM latestGrades WHERE study_course_id = "bvt" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    #for exam in bvt:
    #    text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
    #    # channels and supergroups have a -100 prefix
    #    context.bot.send_message(chat_id="-1001128453828", text=str(text), parse_mode=ParseMode.HTML)

    ## Schiffsbautechnik
    with SQLiteConnection('hsfl_lnn.db') as db:
        sbt = db.query('SELECT * FROM latestGrades WHERE study_course_id = "sbt" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in sbt:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001323289033", text=str(text), parse_mode=ParseMode.HTML)

    ## Schiffsmotorbau
    with SQLiteConnection('hsfl_lnn.db') as db:
        smb = db.query('SELECT * FROM latestGrades WHERE study_course_id = "smb" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in smb:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001171512410", text=str(text), parse_mode=ParseMode.HTML)

    ## Seeverkehr, Nautik und Logistik
    with SQLiteConnection('hsfl_lnn.db') as db:
        snl = db.query('SELECT * FROM latestGrades WHERE study_course_id = "snl" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in snl:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001184473824", text=str(text), parse_mode=ParseMode.HTML)

    ## Business Management
    with SQLiteConnection('hsfl_lnn.db') as db:
        bm = db.query('SELECT * FROM latestGrades WHERE study_course_id = "bm" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in bm:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001466511554", text=str(text), parse_mode=ParseMode.HTML)

    ## Biotechnology and Process Engineering
    with SQLiteConnection('hsfl_lnn.db') as db:
        btpe = db.query('SELECT * FROM latestGrades WHERE study_course_id = "btpe" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in btpe:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001183578983", text=str(text), parse_mode=ParseMode.HTML)

    ## Wind Engineering
    with SQLiteConnection('hsfl_lnn.db') as db:
        we = db.query('SELECT * FROM latestGrades WHERE study_course_id = "we" AND timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for exam in we:
        text = '<a href="' + str(exam[5]) + '">' + str(exam[2]) + '</a>'
        # channels and supergroups have a -100 prefix
        context.bot.send_message(chat_id="-1001493296336", text=str(text), parse_mode=ParseMode.HTML)

def error(update, context):
	return ConversationHandler.END

def main():
    """Run bot."""

    if bot_config.BOT_TOKEN == "INSERT YOUR BOT TOKEN HERE":
        print("Please write TOKEN into 'bot_config.py' file. . .")
        exit()

    # your bot token here
    updater = Updater(token=str(bot_config.BOT_TOKEN), request_kwargs={'read_timeout': 15, 'connect_timeout': 7}, workers=12, use_context=True)

    ### INITIALIZING
    os.system('clear')
    print('######################################')
    print('## HSFL_LatestNewsNotification v0.4 ##')
    print('######################################')
    print()
    print('. . . up and running!')

    def grades_off(update: telegram.Update, context: telegram.ext.CallbackContext):
        grades_handler.enabled = False
        update.message.reply_text('Deactivate Grades Job', reply_markup=markup2)

    def news_off(update: telegram.Update, context: telegram.ext.CallbackContext):
        news_handler.enabled = False # Temporarily disable this job
        update.message.reply_text('Deactivate News Job', reply_markup=markup2)

    def stop(update: telegram.Update, context: telegram.ext.CallbackContext):
        updater.stop()
        update.message.reply_text('Bis bald!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
 
    # Use conversation handler to handle states
    conv_handler = ConversationHandler(
        [CommandHandler('start', start, pass_user_data=True, pass_chat_data=True)],
        { 
<<<<<<< HEAD
		MODUS:	[MessageHandler(Filters.regex('^(Auto)$'), grade_auto_start),
                 MessageHandler(Filters.regex('^(Manually)$'), modus),
=======
		MODUS:	[MessageHandler(Filters.regex('^(Grades)$'), crawl_grades_job),
                 MessageHandler(Filters.regex('^(News)$'), crawl_news_job),
                 MessageHandler(Filters.regex('^(Grades OFF)$'), grades_off),
                 MessageHandler(Filters.regex('^(News OFF)$'), news_off),
>>>>>>> 8a0b9dd6b875ca845c21e438dd4775ecb7934592
				 MessageHandler(Filters.regex('^Abbrechen$'), stop)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)

    # Grades
    grades_handler = CommandHandler('grades', crawl_grades_job)
    updater.dispatcher.add_handler(grades_handler)

    # News
    news_handler = CommandHandler('news', crawl_news_job)
    updater.dispatcher.add_handler(news_handler)

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
