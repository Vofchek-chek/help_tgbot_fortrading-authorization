from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton







# regionbuttons=[{"UA🇺🇦 KZ🇰🇿":"cis"},{"RU🇷🇺MD\n🇲🇩Другая страна❤️":"eu"}]
regionbuttons = InlineKeyboardMarkup(row_width=2)
cis = InlineKeyboardButton('UA🇺🇦 KZ🇰🇿', callback_data='cis')
eu = InlineKeyboardButton('RU🇷🇺MD\n🇲🇩Другая страна❤️', callback_data='eu')
regionbuttons.add(cis,eu)

# rornotbuttons=[{'Готов 🤑':'cisready'}, {'Не готов 👎':'ntready'}]
rornotbuttons = InlineKeyboardMarkup(row_width=2)
ready=InlineKeyboardButton('Готов 🤑',callback_data='cisready')
notready=InlineKeyboardButton('Не готов 👎',callback_data='ntready')
rornotbuttons.add(ready,notready)

# cisroracbuttons=[{'Готово ✅':'ready'},{'Уже есть акк🤨':'cisalraccount'}]
cisroracbuttons = InlineKeyboardMarkup(row_width=2)
cisready = InlineKeyboardButton('Готово ✅',callback_data='ready')
cisnotready = InlineKeyboardButton('Уже есть акк🤨',callback_data='cisalraccount')
cisroracbuttons.add(cisready,cisnotready)

# rbuttons=[{'Готово ✅':'ready'}]
rbuttons = InlineKeyboardMarkup(row_width=1)
ready = InlineKeyboardButton('Готово ✅',callback_data='ready')
rbuttons.add(ready)

# euroracbuttons=[{'Готово ✅':'ready'},{'Уже есть акк🤨':'eualraccount'}]
euroracbuttons = InlineKeyboardMarkup(row_width = 2)
rready=InlineKeyboardButton('Готово ✅',callback_data='ready')
euoldaccaunt=InlineKeyboardButton('Уже есть акк🤨',callback_data='eualraccount')
euroracbuttons.add(rready,euoldaccaunt)

# ntreadybuttons=[{'Готов 🤑':'euready'}, {'Не готов 👎':'ntready'}]
ntreadybuttons = InlineKeyboardMarkup(row_width = 2)
euready = InlineKeyboardButton('Готов 🤑',callback_data='euready')
eunotready = InlineKeyboardButton('Не готов 👎',callback_data='ntready')
ntreadybuttons.add(euready,eunotready)