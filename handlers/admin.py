from create_bot import bot,dp
from aiogram import Dispatcher,types
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher.storage import FSMContext
from config import  ID_ADMIN
from keyboards.kb_admin import kb,back_kb,list_houses
from db import DataBase
from aiogram.dispatcher.filters import Text
class Block(StatesGroup):
    block = State()
    house = State()

db = DataBase('database.db')


@dp.message_handler(commands=['start'])
async def start(msg:types.Message):
    if msg.from_user.id == ID_ADMIN:
        await msg.answer('👇tugmani bosing👇',reply_markup=list_houses)
    else:
        await msg.answer('siz admin emassiz')


@dp.message_handler(Text(equals='uylar ro`yhati'))
async def list_houses_func(msg:types.Message):
    await msg.answer(await db.list_houses_a(),parse_mode='HTML',reply_markup=back_kb)
    await msg.answer(await db.list_houses_b(),parse_mode='HTML',reply_markup=back_kb)
    await msg.answer(await db.list_houses_v(),parse_mode='HTML',reply_markup=back_kb)
    await msg.answer(await db.list_houses_g(),parse_mode='HTML',reply_markup=back_kb)

@dp.message_handler(Text(equals='bloklarga o`tish'))
async def block_choose(msg:types.Message):
    if msg.from_user.id == ID_ADMIN:
        await msg.answer('👇blokni tanlang👇',reply_markup=kb)
        await Block.first()
    else:
        await msg.answer('siz admin emassiz')

@dp.message_handler(state='*',commands=['orqaga'])
@dp.message_handler(Text(equals='orqaga',ignore_case=True),state='*')
async def orqaga_func(message:types.Message,state=FSMContext):
    current = await state.get_state()
    if current is None:
        await start(message)
    else:
        await state.finish()
        await start(message)
@dp.message_handler(state=Block.block)
async def block(msg:types.Message,state=FSMContext):
    if msg.text=='A':
        async with state.proxy() as data:
            data['block']=msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:',reply_markup=back_kb)
    elif msg.text=='Б':
        async with state.proxy() as data:
            data['block']=msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:',reply_markup=back_kb)
    elif msg.text=='В':
        async with state.proxy() as data:
            data['block']=msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:',reply_markup=back_kb)
    elif msg.text=='Г':
        async with state.proxy() as data:
            data['block']=msg.text
        await Block.next()
        await msg.answer('Xonadonning raqamini kiriting:',reply_markup=back_kb)
    else:
        await state.finish()
        await msg.answer('Bunaqa block mavjud emas❌')
        await start(msg)
@dp.message_handler(state=Block.house)
async def house(msg:types.Message,state=FSMContext):
    async with state.proxy() as data:
        if await db.check_house(data['block'],msg.text):
            await msg.answer(await db.info_house(data['block'],msg.text))
            await msg.answer('xonadon raqamini kiriting \nagar orqaga qaytmoqchi bulsangiz pastdagi tugmani bosing👇')
        else:
            await msg.answer(f'{msg.text} raqamli xonadon mavjud emas❌')
            await msg.answer('xonadon raqamini kiriting \nagar orqaga qaytmoqchi bulsangiz pastdagi tugmani bosing👇')

@dp.message_handler(state='*',commands=['отмена'])
@dp.message_handler(Text(equals='отмена',ignore_case=True),state='*')
async def cancel_state(message:types.Message,state=FSMContext):
    current = await state.get_state()
    if current is None:
        return
    else:
        await state.finish()
        await message.answer('операция отменена')

def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(start,commands=['start'])


