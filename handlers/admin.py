import sqlite3

import pandas as pd  # pip install pandas
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InputFile

from config import ID_ADMIN
from create_bot import bot, dp
from db import DataBase
from keyboards.kb_admin import kb, back_kb, list_houses, status_choose, list_houses_kb, excel_kb

conn = sqlite3.connect('database.db')
a = pd.read_sql('SELECT * FROM `A-block`', conn)
b = pd.read_sql('SELECT * FROM `Б-block`', conn)
v = pd.read_sql('SELECT * FROM `В-block`', conn)
g = pd.read_sql('SELECT * FROM `Г-block`', conn)


class Block(StatesGroup):
    block = State()
    house = State()


# block_data= None
class StatusEdit(StatesGroup):
    block = State()
    flat = State()
    status = State()


class ChooseBlock(StatesGroup):
    block = State()


class Excel(StatesGroup):
    block = State()


db = DataBase()

status_list = ['✅', '❌', '⚠️']


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('👇tugmani bosing👇', reply_markup=list_houses)
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(Text(equals='excel file olish'))
async def excel_get(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('blockni tanlang: ', reply_markup=excel_kb)
        await Excel.first()
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(state=Excel.block)
async def excel_send(msg: types.Message, state: FSMContext):
    if msg.text == 'общий excel':
        a = pd.read_sql('SELECT * FROM "A-block"', conn)
        b = pd.read_sql('SELECT * FROM "Б-block"', conn)
        v = pd.read_sql('SELECT * FROM "В-block"', conn)
        g = pd.read_sql('SELECT * FROM "Г-block"', conn)
        with pd.ExcelWriter('output.xlsx') as writer:
            a.to_excel(writer, sheet_name='А-block')
            b.to_excel(writer, sheet_name='Б-block')
            v.to_excel(writer, sheet_name='В-block')
            g.to_excel(writer, sheet_name='Г-block')
        file_xlsx = open('output.xlsx', 'rb')
        await bot.send_document(msg.chat.id, file_xlsx, reply_markup=list_houses)
        await state.finish()
    else:
        a = pd.read_sql(f'SELECT * FROM "{msg.text}-block"', conn)
        a.to_excel(f'result_{msg.text}_block.xlsx', index=True)
        file_xlsx = open(f'result_{msg.text.lower()}_block.xlsx', 'rb')
        await bot.send_document(msg.chat.id, file_xlsx, reply_markup=list_houses)
        await state.finish()


@dp.message_handler(state="*", commands=['orqaga'])
@dp.message_handler(Text(equals='orqaga', ignore_case=True), state="*")
async def orqaga_func(msg: types.Message, state: FSMContext):
    if msg.from_user.id in ID_ADMIN:
        await state.finish()
        await start(msg)
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(Text(equals='status o`zgartirish va uylar ro`yhati'))
async def list_houses_edit_status_func(msg: types.Message, state: FSMContext):
    # await msg.answer(await db.list_houses_a(),parse_mode='HTML',reply_markup=list_houses_kb)
    # await msg.answer(await db.list_houses_b(),parse_mode='HTML',reply_markup=list_houses_kb)
    # await msg.answer(await db.list_houses_v(),parse_mode='HTML',reply_markup=list_houses_kb)
    # await msg.answer(await db.list_houses_g(),parse_mode='HTML',reply_markup=list_houses_kb)
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('👇tugmani tanlang👇', reply_markup=list_houses_kb)
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(Text(equals='uylar ro`yhati'))
async def list_houses_func(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await ChooseBlock.first()
        await msg.answer('👇tugmani bosing👇', reply_markup=kb)
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(state=ChooseBlock.block)
async def choose_block(msg: types.Message, state: FSMContext):
    if msg.text == 'A':
        await msg.answer(await db.list_houses_a(), parse_mode='HTML', reply_markup=list_houses_kb)
        await state.finish()
    elif msg.text == 'Б':
        await msg.answer(await db.list_houses_b(), parse_mode='HTML', reply_markup=list_houses_kb)
        await state.finish()
    elif msg.text == 'В':
        await msg.answer(await db.list_houses_v(), parse_mode='HTML', reply_markup=list_houses_kb)
        await state.finish()
    elif msg.text == 'Г':
        await msg.answer(await db.list_houses_g(), parse_mode='HTML', reply_markup=list_houses_kb)
        await state.finish()


@dp.message_handler(Text('statusni almashtirish'))
async def edit_status(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('statusni amashtirish uchun blokni tanlang', reply_markup=kb)
        await StatusEdit.first()
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(state=StatusEdit.block)
async def statusedit_load(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['block'] = msg.text
    await StatusEdit.next()
    await msg.answer('statusni almashtirish uchun honadon raqamini kiriting: ')


@dp.message_handler(state=StatusEdit.flat)
async def statusedit_load_house(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if await db.check_house(data['block'], msg.text):
            data['house'] = msg.text
            await StatusEdit.next()
            await msg.answer('statusni almashtirish uchun statusni tanlang: ', reply_markup=status_choose)
        else:
            await msg.answer(f'{msg.text} raqamli xonadon mavjud emas❌')
            await msg.answer(
                'xonadon raqamini kiriting \nagar orqaga qaytmoqchi bulsangiz pastdagi tugmani bosing👇')


@dp.message_handler(state=StatusEdit.status)
async def statusedit_load_status(msg: types.Message, state: FSMContext):
    if msg.text in status_list:
        async with state.proxy() as data:
            data['status'] = msg.text
            await msg.answer(await db.status_edit(data['block'], data['house'], data['status']))
            await start(msg)
            await state.finish()
    else:
        await msg.answer(f'mavjud bo`lmagan {msg.text} status kiritildi')
        await state.finish()
        await start(msg)


@dp.message_handler(Text(equals='bloklarga o`tish'))
async def block_choose(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('👇blokni tanlang👇', reply_markup=kb)
        await Block.first()
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(state=Block.block)
async def block(msg: types.Message, state: FSMContext):
    global block_data
    global house_data
    block_data = None
    house_data = None
    if msg.text == 'A':
        async with state.proxy() as data:
            data['block'] = msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:', reply_markup=back_kb)
        block_data = msg.text
    elif msg.text == 'Б':
        async with state.proxy() as data:
            data['block'] = msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:', reply_markup=back_kb)
        block_data = msg.text
    elif msg.text == 'В':
        async with state.proxy() as data:
            data['block'] = msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:', reply_markup=back_kb)
        block_data = msg.text
    elif msg.text == 'Г':
        async with state.proxy() as data:
            data['block'] = msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:', reply_markup=back_kb)
        block_data = msg.text
    else:
        await state.finish()
        await msg.answer('Bunaqa block mavjud emas❌')
        await start(msg)


@dp.message_handler(state=Block.house)
async def house(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if await db.check_house(data['block'], msg.text):
            for i in await db.info_house(data['block'], msg.text):
                file = InputFile(f'media/{i[5]}.jpg')
                await msg.answer_photo(file)
                await msg.answer(
                    f'{i[0]}-blok\n{i[1]}-podezd\n{i[2]}-qavat\n{i[3]}-honadon\n{i[4]} xonali\n{i[5]} kv.m\n{i[6]}-kv.m narxi\nstatus:{i[7]}\n ',
                    reply_markup=back_kb)

        else:
            await msg.answer(f'{msg.text} raqamli xonadon mavjud emas❌')
            await msg.answer(
                'xonadon raqamini kiriting \nagar orqaga qaytmoqchi bulsangiz pastdagi tugmani bosing👇')


@dp.message_handler(state='*', commands=['отмена'])
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_state(message: types.Message, state: FSMContext):
    if message.from_user.id in ID_ADMIN:
        await state.finish()
        await message.answer('операция отменена')
    else:
        await message.answer('siz admin emassiz')


async def oshibka(msg: types.Message):
    await msg.answer('/start ni bosing')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
