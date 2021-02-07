from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from parse.parse_html import get_html
from keyboards.inline.choice_buttons import *
from loader import dp, bot
from asyncpg import Connection, Record
import emoji

cgid = None                # параметры передаваемые с url


@dp.message_handler(Command('items'))
async def show_items(message: Message):
    await message.answer(text=GENDER_SELECT, reply_markup=choose_gender)


@dp.callback_query_handler(text=[MEN, WOMEN, KIDS_BOYS, KIDS_GIRLS])
async def gender_category(call: CallbackQuery):
    global cgid
    cgid = call.data
    await call.message.answer(text=TYPE_SELECT, reply_markup=choose_category)


@dp.callback_query_handler(text=[SHOES, CLOTHING, ACCESSORIES])
async def items_category(call: CallbackQuery):
    global cgid
    if cgid[-1:] == '-':               # проверяем удаление последнего параметра переданного в url при нажатии на cancel
        cgid += call.data
    if cgid == MEN + SHOES:
        await call.message.answer(text=CATEGORY_SELECT, reply_markup=men_shoes_category)
    elif cgid == WOMEN + SHOES:
        await call.message.answer(text=CATEGORY_SELECT, reply_markup=women_shoes_category)
    elif cgid == MEN + CLOTHING:
        await call.message.answer(text=CATEGORY_SELECT, reply_markup=mens_clothing_category)
    elif cgid == WOMEN + CLOTHING:
        await call.message.answer(text=CATEGORY_SELECT, reply_markup=women_clothing_category)
    elif call.data == ACCESSORIES:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_accessories)
    elif cgid == KIDS_GIRLS + CLOTHING or cgid == KIDS_BOYS + CLOTHING:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_kids_clothing)
    elif cgid == KIDS_BOYS + SHOES or cgid == KIDS_GIRLS + SHOES:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_kids_shoes)
    print(cgid)


@dp.callback_query_handler(text=[
    LIFESTYLE, CLASSICS, TRAINING_GYM, RUNNING, BASKETBALL_HERITAGE,
    BASKETBALL_PERFORMANCE, SLIDES_SANDALS, MOTOSPORT, SHORTS,
    SWEATSHIRTS_HOODIES, T_SHIRTS_TOPS, TRACKSUITS, JACKETS,
    PANTS, LEGGINGS, BRAS
])
async def choice_category(call: CallbackQuery):
    global cgid
    cgid += call.data
    if call.data == T_SHIRTS_TOPS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_tshirts)
    elif call.data == LIFESTYLE:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_lifestyle)
    elif call.data == CLASSICS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_classics)
    elif call.data == TRAINING_GYM:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_training)
    elif call.data == RUNNING:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_running)
    elif call.data == SLIDES_SANDALS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_slides)
    elif call.data == BASKETBALL_PERFORMANCE:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_basketball_p)
    elif call.data == BASKETBALL_HERITAGE:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_basketball_h)
    elif call.data == MOTOSPORT:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_motosport)
    elif call.data == SWEATSHIRTS_HOODIES:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_hoodies)
    elif call.data == SHORTS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_shorts)
    elif call.data == TRACKSUITS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_tracksuits)
    elif call.data == PANTS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_pants)
    elif call.data == LEGGINGS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_leggings)
    elif call.data == BRAS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_bras)
    elif call.data == JACKETS:
        await call.message.answer(text=PRICE_SELECT, reply_markup=choose_price_jackets)
    print(cgid)


@dp.callback_query_handler(text=PRICES_LIST)
async def get_price(call: CallbackQuery):
    global cgid
    item_list = get_html(URL, cgid, call.data)
    count = 0
    for item in item_list:
        await call.message.answer_photo(
            item['img'], f"{item['name']}\n {item['price']} {item['currency']}",
            reply_markup=get_url_button(item['href'])
        )


@dp.callback_query_handler(text=CANCEL)
async def back(call: CallbackQuery):
    global cgid
    edit_cgid = cgid.split('-')[0] + '-'      # удаляем последнее изменение передаваемое в параматры url
    cgid = edit_cgid                          # перезаписываем параметры передаваемые в url
    await call.message.delete()


@dp.callback_query_handler(text=PRICE_CANCEL)
async def back(call: CallbackQuery):
    global cgid
    edit_cgid = cgid.split('-')[0] + '-' + cgid.split('-')[1]      # удаляем последнее изменение передаваемое в параматры url
    cgid = edit_cgid                                               # перезаписываем параметры передаваемые в url
    await call.message.delete()
