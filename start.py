import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from complex import Complex
import datetime
import tg_logger

token = "5612298789:AAGwfSSMFliZLFvjPQXVbEV6XYGcIzYaX7w"
users = []
tg_files_logger = tg_logger.TgFileLogger(
    token=token,
    users=users,
)
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def startCommand(update: Update, context: CallbackContext):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! Что ты хочешь?\nПоработать с рациональными числами? Жми /racio !\nПоработать с комплексными числами? Жми /complex !')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")

def startCommand_racio(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Посчитать сумму', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Умножение', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Деление', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Разность', callback_data='buttonD')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])

    update.message.reply_text('Чтобы начать работу, выберите одно из возможных действий',
                              reply_markup=markup)
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")
    return callback

def sum_command_racio(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def mult_command_racio(update: Update, context: CallbackContext):
    a = int(context.args[0]) * int(context.args[1])
    update.message.reply_text(f'{int(context.args[0])} * {int(context.args[1])} = {a}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def del_command_racio(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {round((x / y), 2)}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def razn_command_racio(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")



def startCommand_complex(update: Update, context: CallbackContext):
    buttonE = telegram.InlineKeyboardButton('Посчитать сумму', callback_data='buttonE')
    buttonF = telegram.InlineKeyboardButton('Посчитать разность', callback_data='buttonF')
    buttonG = telegram.InlineKeyboardButton('Посчитать произведение', callback_data='buttonG')
    buttonH = telegram.InlineKeyboardButton('Разделить', callback_data='buttonH')
    buttonI = telegram.InlineKeyboardButton('Модуль', callback_data='buttonI')
    buttonJ = telegram.InlineKeyboardButton('Угол', callback_data='buttonJ')
    buttonK = telegram.InlineKeyboardButton('Комлпексно-сопряженное', callback_data='buttonK')
    buttonL = telegram.InlineKeyboardButton('Логарифм', callback_data='buttonL')

    markup = telegram.InlineKeyboardMarkup(
        inline_keyboard=[[buttonE], [buttonF], [buttonG], [buttonH], [buttonI], [buttonJ], [buttonK], [buttonL]])
    update.message.reply_text(
        'Чтобы начать работу, необходимо ввести данные двух комплексных чисел. Формат комлексного числа: x = a + bj, y = a + bj.',
        reply_markup=markup)
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")
    return callback


def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data

    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Введите /plus числа через пробел: ')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Введите /mr числа через пробел: ')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Введите /dr числа через пробел: ')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Введите /minus числа через пробел: ')

    if variant == 'buttonE':
        query.answer()
        query.edit_message_text(text='Введите +: и через пробел xa, xb, ya, yb')
    if variant == 'buttonF':
        query.answer()
        query.edit_message_text(text='Введите -: и через пробел xa, xb, ya, yb')
    if variant == 'buttonG':
        query.answer()
        query.edit_message_text(text='Введите /mult и через пробел xa, xb, ya, yb')
    if variant == 'buttonH':
        query.answer()
        query.edit_message_text(text='Введите /del и через пробел xa, xb, ya, yb')
    if variant == 'buttonI':
        query.answer()
        query.edit_message_text(text='Введите /mod и через пробел xa, xb')
    if variant == 'buttonJ':
        query.answer()
        query.edit_message_text(text='Введите /angle и через пробел xa, xb')
    if variant == 'buttonK':
        query.answer()
        query.edit_message_text(text='Введите /conj и через пробел xa, xb')
    if variant == 'buttonL':
        query.answer()
        query.edit_message_text(text='Введите /log и через пробел xa, xb')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def sum_command_complex(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    ya = int(items[3])
    yb = int(items[4])
    update.message.reply_text(f'сумма: x = {xa} + {xb}j и y = {ya} + {yb}j :  {complex(xa, xb) + (complex(ya, yb))} ')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def razn_command_complex(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    ya = int(items[3])
    yb = int(items[4])
    update.message.reply_text(f'разность: x = {xa} + {xb}j и y = {ya} + {yb}j :  {complex(xa, xb) - (complex(ya, yb))}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def mult_command_complex(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    ya = int(items[3])
    yb = int(items[4])
    update.message.reply_text(
        f'произведение: x = {xa} + {xb}j и y = {ya} + {yb}j :  {complex(xa, xb) * (complex(ya, yb))} ')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def del_command_complex(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    ya = int(items[3])
    yb = int(items[4])
    update.message.reply_text(f'частное: x = {xa} + {xb}j и y = {ya} + {yb}j :  {complex(xa, xb) / (complex(ya, yb))}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def mod_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    x = Complex(xa, xb)
    update.message.reply_text(f'модуль: x = {xa} + {xb}j :  {x.mod()}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def angle_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    x = Complex(xa, xb)
    update.message.reply_text(f'угол: x = {xa} + {xb}j :  {x.angle()}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def conj_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    x = Complex(xa, xb)
    update.message.reply_text(f'Комлпексно-сопряженное: x = {xa} + {xb}j :  {x.conjugate()}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")


def log_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    xa = int(items[1])
    xb = int(items[2])
    x = Complex(xa, xb)
    update.message.reply_text(f'Логарифм: x = {xa} + {xb}j :  {x.log()}')
    with open('TestBot.log', 'a',encoding="utf-8") as f:
        f.write(f"{str(datetime.datetime.now())}, {update.effective_user.full_name}, {update.effective_chat.username}, {update.effective_message.text}\n")
    tg_files_logger.send('TestBot.log', "TestBot.log")

start_command_handler_complex = CommandHandler('complex', startCommand_complex)
sum_handler_complex = MessageHandler(Filters.regex(r'\+:'), sum_command_complex)
razn_handler_complex = MessageHandler(Filters.regex(r'\-:'), razn_command_complex)
mult_handler_complex = MessageHandler(Filters.regex("mult"), mult_command_complex)
del_handler_complex = MessageHandler(Filters.regex("del"), del_command_complex)
mod_handler = MessageHandler(Filters.regex("mod"), mod_command)
angle_handler = MessageHandler(Filters.regex("angle"), angle_command)
conj_handler = MessageHandler(Filters.regex("conj"), conj_command)
log_handler = MessageHandler(Filters.regex("log"), log_command)
start_command_handler = CommandHandler('start', startCommand)
start_command_handler_racio = CommandHandler('racio', startCommand_racio)
sum_handler_racio = MessageHandler(Filters.regex('plus'), sum_command_racio)
razn_handler_racio = MessageHandler(Filters.regex('minus'), razn_command_racio)
mult_handler_racio = CommandHandler('mr', mult_command_racio)
del_handler_racio = CommandHandler('dr', del_command_racio)


callback_buttom_handler = CallbackQueryHandler(callback=callback, pattern=None, run_async=False)




dispatcher.add_handler(start_command_handler_racio)
dispatcher.add_handler(start_command_handler_complex)
dispatcher.add_handler(sum_handler_complex)

dispatcher.add_handler(razn_handler_complex)
dispatcher.add_handler(mult_handler_complex)
dispatcher.add_handler(del_handler_complex)
dispatcher.add_handler(mod_handler)
dispatcher.add_handler(angle_handler)
dispatcher.add_handler(conj_handler)
dispatcher.add_handler(log_handler)
dispatcher.add_handler(sum_handler_racio)
dispatcher.add_handler(razn_handler_racio)
dispatcher.add_handler(mult_handler_racio)
dispatcher.add_handler(del_handler_racio)
dispatcher.add_handler(start_command_handler)

dispatcher.add_handler(callback_buttom_handler)

updater.start_polling()
updater.idle()


