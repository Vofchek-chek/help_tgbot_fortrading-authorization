# -*- coding: utf8 -*-
import time
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards as kb
import csv
import traceback


count=10
token='2016291523:AAGjdHizngiA3ZcXk6z1ayw9KNU-CPp268c'#write your bot token here
greeting="Привет, <b>бро</b>👋🏻\nПодберем для тебя биржу📈\nТы откуда❓"
cisgrtxt="<b>Отлично, <b>земляк</b> 👍</b>\n\nПеред вступлением в закрытый VIP проясним пару моментов,\nчто бы вдруг ты не тратил ни своё, ни наше время 🔥\n\nVipTradeClub - полностью бесплатный❗️\nЗа сигналы и проход✅ денег никто не берет❌\n\nНо, что бы начать поднимать вместе с командой 💸, нужно выполнить некоторые инструкции для прохода в VIP CLUB❗️\n\nГотов выслушать инструкции❓\nНачнём поднимать вместе?💰"
eugrtxt="<b>Отлично 👍</b>\n\nПеред вступлением в закрытый VIP проясним пару моментов,\nчто бы вдруг ты не тратил ни своё, ни наше время 🔥\n\nVipTradeClub - полностью бесплатный❗️\nЗа сигналы и проход✅ денег никто не берет❌\n\nНо, что бы начать поднимать вместе с командой 💸, нужно выполнить некоторые инструкции для прохода в VIP CLUB❗️\n\nГотов выслушать инструкции❓\nНачнём поднимать вместе?💰"
cisinstruction="Чтобы залететь в закрытый VIP CLUB - выполни инструкцию🚨\n\n♻️Инструкция:\nЗайди по кнопке ⬇️\nИ создай новый акк 🤝\n\n<a href='https://binomo.com?a=50118e8634c5'><b>👉🏻СОЗДАТЬ АККАУНТ👈</b></a>  \n\nИ после регистрации, жми кнопку «Готово ✅»👇\n\n  Жду бро😎"
euinstruction="Чтобы залететь в закрытый VIP CLUB - выполни инструкцию🚨\n\n♻️Инструкция:\nЗайди по кнопке ⬇️\nИ создай новый акк 🤝\n\n<a href='https://quotex-broker.com/sign-up/?lid=80345'><b>👉🏻СОЗДАТЬ АККАУНТ👈</b></a>  \n\nИ после регистрации, жми кнопку «Готово ✅»👇\n\n  Жду бро😎"
cisoldaccaunt="<b>Бро🤝</b>\nЭто старый аккаунт, он не пройдёт модерацию в VIP😔\n\n⚠️Чтобы залететь в закрытый VIP CLUB и БЕСПЛАТНО получать <b>50 сигналов в сутки с проходом 94%</b>✅\nВыполни инструкцию🚨\n\n♻️Инструкция:\n\n1. Выйди со старого аккаунта 👍\n2.❗️Перезайди в телеграмм(ВАЖНО)❗️\n3. Зайди по кнопке ⬇️\n4. И создай новый акк 🤝\n\n<a href='https://binomo.com?a=50118e8634c5'><b>👉🏻СОЗДАТЬ АККАУНТ👈</b></a>\n\nИ после регистрации, жми кнопку «Готово ✅»👇\n\nЖду бро😎"
euoldaccaunt="<b>Бро🤝</b>\nЭто старый аккаунт, он не пройдёт модерацию в VIP😔\n\n⚠️Чтобы залететь в закрытый VIP CLUB и БЕСПЛАТНО получать <b>50 сигналов в сутки с проходом 94%</b>✅\nВыполни инструкцию🚨\n\n♻️Инструкция:\n\n1. Выйди со старого аккаунта 👍\n2.❗️Перезайди в телеграмм(ВАЖНО)❗️\n3. Зайди по кнопке ⬇️\n4. И создай новый акк 🤝\n\n<a href='https://quotex-broker.com/sign-up/?lid=80345'><b>👉🏻СОЗДАТЬ АККАУНТ👈</b></a>\n\nИ после регистрации, жми кнопку «Готово ✅»👇\n\nЖду бро😎"
ending="Отлично 👍\n\nТеперь скинь ID от нового аккаунта нашему менеджеру 👉🏻@supp4you \n\nОн его проверит и внесёт вас в VIP❤️"
error="Некорректное действие 🥴\n❗️Бро, по всем вопросам пиши нашему менеджеру 👉🏻\n@supp4you"
support="По всем вопросам\n👉🏻@supp4you"
forwardmessage='Следующее отправленнное вами сообщение будет отправлено пользователям вашего бота'
adminid=[1974035984, 833231928] #mian : 1974035984
users=[]

asyncbot=telebot.AsyncTeleBot(token)
bot = Bot(token)
dp = Dispatcher(bot)
forwardmessagemode=False

def listofusers():
    users=[]
    with open('userdb.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(row[0])
    return users

def blckedusers():
    blusers=[]
    with open('blockedusers.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            blusers.append(row[0])
    return len(set(blusers))


def global_stats():
    return f'<b>Общее количество пользователей:</b>{len(set(listofusers()))}\n<b>Пользователи, заблокировавшие бота:</b>{blckedusers()}'

@dp.message_handler(commands=['start','support','message','admin'])
async def answer(message: types.Message):    
    if message.text == '/start':     
        await bot.send_message(message.chat.id,text=greeting,reply_markup=kb.regionbuttons,parse_mode = 'HTML')
        if str(message.chat.id) not in listofusers(): 
            with open('userdb.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([str(message.chat.id)])
    elif message.text == '/support':
        await bot.send_message(message.chat.id,support,parse_mode = 'HTML')
    elif message.text == '/message' and message.chat.id in adminid:
        await bot.send_message(message.chat.id,text=forwardmessage)
        global forwardmessagemode
        forwardmessagemode=True
    elif message.text == '/admin' and message.chat.id in adminid:
        with open('stats.png','rb') as pfile:

            await bot.send_photo(message.chat.id,pfile,caption=global_stats(),parse_mode='HTML')
    else:
        await bot.send_message(message.chat.id,error)


@dp.message_handler(content_types=['text'])
async def text_message(message):
    global forwardmessagemode
    if message.chat.id in adminid and forwardmessagemode  and message.text !='/message':
        forwardmessagemode=False
        with open('messagetosubs.txt','w') as file:
            file.write(str(message.message_id))
        
    else:await bot.send_message(message.chat.id,error)


@dp.callback_query_handler(lambda c: c.data)
async def callback_handler(call:types.CallbackQuery):
    if call.data == "cis":
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=cisgrtxt, reply_markup=kb.rornotbuttons,parse_mode = 'HTML')
    elif call.data == 'eu':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=eugrtxt, reply_markup=kb.ntreadybuttons,parse_mode = 'HTML')
    elif call.data == 'cisready':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=cisinstruction, reply_markup=kb.cisroracbuttons,parse_mode = 'HTML',disable_web_page_preview = True)
    elif call.data == 'euready':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=euinstruction, reply_markup=kb.euroracbuttons,parse_mode = 'HTML',disable_web_page_preview = True)
    elif call.data == 'cisalraccount':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=cisoldaccaunt, reply_markup=kb.rbuttons,parse_mode = 'HTML',disable_web_page_preview = True)
    elif call.data == 'eualraccount':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=euoldaccaunt, reply_markup=kb.rbuttons,parse_mode = 'HTML',disable_web_page_preview = True)
    elif call.data == 'ready':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text=ending) 
    elif call.data == 'ntready':
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id,text="Жми /start и подумай ещё раз😏💵")
    else:
        await bot.send_message(call.message.chat.id,text=error)           

executor.start_polling(dp)