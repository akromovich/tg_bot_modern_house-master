from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
k_1 = KeyboardButton('A')
k_2 = KeyboardButton('Б')
k_3 = KeyboardButton('В')
k_4 = KeyboardButton('Г')
kb.add(k_1,k_2,k_3,k_4)
back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
k_5= KeyboardButton('orqaga')
back_kb.add(k_5)

list_houses = ReplyKeyboardMarkup(resize_keyboard=True)
l_1 = KeyboardButton('uylar ro`yhati')
l_2 = KeyboardButton('bloklarga o`tish')
list_houses.add(l_1,l_2)