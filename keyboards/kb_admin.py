from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

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
l_1 = KeyboardButton('status o`zgartirish va uylar ro`yhati')
l_2 = KeyboardButton('bloklarga o`tish')
list_houses.add(l_1,l_2)

status_choose= ReplyKeyboardMarkup(resize_keyboard=True)
st_1 =KeyboardButton('✅')
st_2 =KeyboardButton('❌')
st_3 =KeyboardButton('⚠️')
st_4 =KeyboardButton('orqaga')
status_choose.add(st_1,st_2,st_3,st_4)

list_houses_kb = ReplyKeyboardMarkup(resize_keyboard=True)
ls_1 = KeyboardButton('orqaga')
ls_2 = KeyboardButton('statusni almashtirish')
ls_3 = KeyboardButton('uylar ro`yhati')
ls_4 = KeyboardButton('excel file olish')
list_houses_kb.add(ls_3,ls_2,ls_4).add(ls_1)