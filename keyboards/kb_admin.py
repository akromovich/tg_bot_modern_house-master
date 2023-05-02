from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
k_1 = KeyboardButton('A')
k_2 = KeyboardButton('Б')
k_3 = KeyboardButton('В')
k_4 = KeyboardButton('Г')
back_k_5= KeyboardButton('orqaga')
kb.add(k_1,k_2,k_3,k_4).add(back_k_5)
back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
k_5= KeyboardButton('orqaga')
back_kb.add(k_5)

list_houses = ReplyKeyboardMarkup(resize_keyboard=True)
l_1 = KeyboardButton('uylar ro`yhati')
l_2 = KeyboardButton('bloklarga o`tish')
list_houses.add(l_1,l_2)

status_choose= ReplyKeyboardMarkup(resize_keyboard=True)
st_1 = ('✅')
st_2 = ('❌')
st_3 = ('⚠️')
st_4 = ('orqaga')
status_choose.add(st_1,st_2,st_3,st_4)
