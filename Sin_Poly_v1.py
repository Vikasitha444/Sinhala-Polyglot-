#!/usr/bin/python3.9
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
#with webhook
#pip install googletrans==3.1.0a0

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime
from googletrans import Translator
# Enable logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


api_key = "5332873438:AAHNHdod23zMkASjgqzLl4MRw9_uPkg3_p0"



iso_639_choices = [('ab', 'Abkhaz'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('ca', 'Catalan; Valencian'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('ny', 'Chichewa; Chewa; Nyanja'), ('zh', 'Chinese'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Divehi; Maldivian;'), ('nl', 'Dutch'), ('dz', 'Dzongkha'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('ff', 'Fula'), ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek, Modern'), ('gn', 'Guaraní'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('he', 'Hebrew (modern)'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ie', 'Interlingue'), ('ga', 'Irish'), ('ig', 'Igbo'), ('ik', 'Inupiaq'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('ki', 'Kikuyu, Gikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz, Kyrgyz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('kj', 'Kwanyama, Kuanyama'), ('la', 'Latin'), ('lb', 'Luxembourgish'), ('lg', 'Luganda'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('lv', 'Latvian'), ('gv', 'Manx'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Māori'), ('mr', 'Marathi (Marāṭhī)'), ('mh', 'Marshallese'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('nv', 'Navajo, Navaho'), ('nb', 'Norwegian Bokmål'), ('nd', 'North Ndebele'), ('ne', 'Nepali'), ('ng', 'Ndonga'), ('nn', 'Norwegian Nynorsk'), ('no', 'Norwegian'), ('ii', 'Nuosu'), ('nr', 'South Ndebele'), ('oc', 'Occitan'), ('oj', 'Ojibwe, Ojibwa'), ('cu', 'Old Church Slavonic'), ('om', 'Oromo'), ('or', 'Oriya'), ('os', 'Ossetian, Ossetic'), ('pa', 'Panjabi, Punjabi'), ('pi', 'Pāli'), ('fa', 'Persian'), ('pl', 'Polish'), ('ps', 'Pashto, Pushto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Kirundi'), ('ro', 'Romanian, Moldavan'), ('ru', 'Russian'), ('sa', 'Sanskrit (Saṁskṛta)'), ('sc', 'Sardinian'), ('sd', 'Sindhi'), ('se', 'Northern Sami'), ('sm', 'Samoan'), ('sg', 'Sango'), ('sr', 'Serbian'), ('gd', 'Scottish Gaelic'), ('sn', 'Shona'), ('si', 'Sinhala (සිංහල)'), ('sk', 'Slovak'), ('sl', 'Slovene'), ('so', 'Somali'), ('st', 'Southern Sotho'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('bo', 'Tibetan'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ty', 'Tahitian'), ('ug', 'Uighur, Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('fy', 'Western Frisian'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang, Chuang'), ('zu', 'Zulu'),]

translator = Translator()


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f"<b>Send</b>  or forward your text. 👍😉\nඔබේ වාක්‍ය <b>එවන්න</b>, නැතිනම් <b>ෆෝවර්ඩ් කරන්න</b>",parse_mode= ParseMode.HTML)


    chat_id = update.message.chat_id
    group_id = update.message.chat.id
    type = update.message.chat.type
    group_name = update.message.chat.title
    reyplyed_user_fristName = update.message.from_user.first_name
    reyplyed_user_username = update.message.from_user.username
    reyplyed_user_user_language = update.message.from_user.language_code
    reyplyed_user_user_id = update.message.from_user.id

    context.bot.send_message(chat_id=378984038, text =f'''<u><b>Report released - New bot user</b></u>\n\n<b>Status :- New Bot User</b>\n<i>(A new user starts the bot at now)</i>\n\nName :- {reyplyed_user_fristName}\nusername:- @{reyplyed_user_username}\nChat ID :- {chat_id}\nChat type :- {type}\nGroup :- {group_name}\nlanguage:-{reyplyed_user_user_language}\n\n<code>{datetime.datetime.now().strftime("%Y/%m/%d")}\n{datetime.datetime.now().strftime("%A")}\n{datetime.datetime.now().strftime("%H:%m %p")}</code>''', parse_mode=ParseMode.HTML)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(f"ඔබට මෙම බොට් පාවිච්චි කිරීමට කිසිදු විධානයක් භාවිතා කල යුතු නැත. සරලව ඔබගේ වාක්‍ය ටයිප් කරන්න. නැත්නම් ෆෝවර්ඩ් කරන්න.\n\n\nඔබේ අදහසත් අපිට කියන්න 📥\n@Me_llamo_TOKIO\npawanvikasitha2001@gmail.com\n\nCreated by: <b><i>Pawan Vikasitha</i></b> also known as <b><i>@Me_llamo_TOKIO</i></b>\nConcept by: <b><i>Tharusha Damsak</i></b> also known as <b><i>@Brian_TD</i></b>",parse_mode= ParseMode.HTML)


def trancelate(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    group_id = update.message.chat.id
    type = update.message.chat.type
    group_name = update.message.chat.title
    reyplyed_user_fristName = update.message.from_user.first_name
    reyplyed_user_username = update.message.from_user.username
    reyplyed_user_user_language = update.message.from_user.language_code
    reyplyed_user_user_id = update.message.from_user.id


    text_sent_by_user = update.message.text
    detected_language = translator.detect(text_sent_by_user).lang

    tranelating_text = translator.translate(text_sent_by_user, dest="si").text
    tranelating_pronounciation = translator.translate(text_sent_by_user, dest="si").pronunciation




    language_global = ""
    for iso_language in iso_639_choices:
        for detected_language_one_by_one in detected_language:
            if iso_language[0] == detected_language_one_by_one:
                language_global = language_global + iso_language[1]

        if iso_language[0] == detected_language:
            language_global = language_global + iso_language[1]

    #print("{}".format(translator.translate(language_global,dest="si").text))
    #print("{}\n{}".format(tranelating_text,tranelating_pronounciation))
    update.message.reply_text(f"සිංහල පරිවර්තනය👇\n<b>{tranelating_text}</b>\n\n\nඋච්චාරණය (Accent) 🗣 : \n<i>{tranelating_pronounciation}</i>\n\nභාෂාව (language) 🗨 : \n<i>{translator.translate(language_global,dest='si').text} ==> සිංහල</i>",parse_mode= ParseMode.HTML)



def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(api_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, trancelate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
