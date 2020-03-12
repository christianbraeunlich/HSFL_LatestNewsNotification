#!/usr/bin/env python3

import pytest

def test_funcfast():
    time.sleep(0.1)

def test_funcslow():
    time.sleep(0.3)

# Telegram-API
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

from HSFL_LNN import bot_config

# Libraries
import sys, os, threading, logging
import datetime, time, sched
import sqlite3

# Internal
from HSFL_LNN.SQLiteConnection import SQLiteConnection

### INITIALIZING
os.system('clear')
print('######################################')
print('## HSFL_LatestNewsNotification v0.3 ##')
print('######################################')
print()
print('. . . up and running!')

MODUS = range(1)

### MODUS PANEL ###
keyboard2 =	[['Auto', 'Manually', 'Abbrechen']
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

def news(update, context):
    os.system("scrapy crawl hsfl_latestnewsnotify")
    with SQLiteConnection('hsfl_lnn.db') as db:
        my_text = db.query('SELECT * FROM latestNews WHERE timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
        for text in my_text:
            context.bot.send_message(chat_id=update.message.chat_id, text=text , parse_mode=ParseMode.HTML)
    update.message.reply_text('', reply_markup=markup3)
    return MAINMENUE

def grade(update, context):
    os.system("scrapy crawl hsfl_latestgradesnotify")
    with SQLiteConnection('hsfl_lnn.db') as db:
        my_text = db.query('SELECT * FROM latestGrades WHERE timestamp BETWEEN ? AND ?', (datetime.datetime.now() - datetime.timedelta(seconds=60), datetime.datetime.now() + datetime.timedelta(seconds=60) ) )
    for text in my_text:
        context.bot.send_message(chat_id=update.message.chat_id, text=text , parse_mode=ParseMode.HTML)
    update.message.reply_text('', reply_markup=markup3)
    return MAINMENUE

def grade_auto_start(update, context):
    thread = threading.Thread(target=run(update, context), args=())
    thread.daemon = True                            # Daemonize thread
    thread.start()                                  # Start the execution
    update.message.reply_text('', reply_markup=markup3)
    return MAINMENUE

def run(update, context):
    while True:
        print('Get new Grades . . .')
        os.system("scrapy crawl hsfl_latestgradesnotify")

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

        time.sleep(60*1)

def modus(update, context):
    my_text = 'Select A Modus'
    context.bot.send_message(chat_id=update.message.chat_id, text=my_text , parse_mode=ParseMode.HTML)
    update.message.reply_text('MODUS', reply_markup=markup2)
    return MODUS

def stop(update, context):
	update.message.reply_text('Bis bald mit', reply_markup=ReplyKeyboardRemove())
	return ConversationHandler.END

def error(update, context):
	return ConversationHandler.END 

def do_something(sc): 
    print("Doing stuff...")
    # do your stuff

def main():
    updater = Updater(str(bot_config.BOT_TOKEN), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
 
    # Use conversation handler to handle states
    conv_handler = ConversationHandler(
        [CommandHandler('start', start, pass_user_data=True, pass_chat_data=True)],
        { 
		MODUS:	[MessageHandler(Filters.regex('^(Auto)$'), grade_auto_start),
                 MessageHandler(Filters.regex('^(Manually)$'), modus),
				 MessageHandler(Filters.regex('^Abbrechen$'), stop)],
        },
        [CommandHandler('stop', stop)],
    )

    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler(
        'start', start, pass_user_data=True, pass_chat_data=True))
    
    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    s = sched.scheduler(time.time, time.sleep)
    s.enter(60, 1, do_something, (s,))
    s.run()

if __name__ == '__main__':
    main()
