from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from parse.constants import *
import emoji


def get_url_button(url):
    url_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=TO_SITE + emoji.emojize(' :rocket:'), url=url)
            ]
        ]
    )
    return url_button


choose_gender = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'MEN {emoji.emojize(":man:", use_aliases=True)}', callback_data=MEN),
            InlineKeyboardButton(text=f'WOMEN {emoji.emojize(":woman:", use_aliases=True)}', callback_data=WOMEN)
        ],
        [
            InlineKeyboardButton(text=f'BOYS {emoji.emojize(":boy:", use_aliases=True)}', callback_data=KIDS_BOYS),
            InlineKeyboardButton(text=f'GIRLS {emoji.emojize(":girl:", use_aliases=True)}', callback_data=KIDS_GIRLS)
        ]
    ]
)

choose_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='SHOES', callback_data=SHOES),
            InlineKeyboardButton(text='CLOTHING', callback_data=CLOTHING),
            InlineKeyboardButton(text='ACCESSORIES', callback_data=ACCESSORIES)
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

men_shoes_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='LIFESTYLE', callback_data=LIFESTYLE),
            InlineKeyboardButton(text='CLASSICS', callback_data=CLASSICS),
            InlineKeyboardButton(text='RUNNING', callback_data=RUNNING)
        ],
        [
            InlineKeyboardButton(text='TRAINING & GYM', callback_data=TRAINING_GYM),
            InlineKeyboardButton(text='SLIDES & SANDALS', callback_data=SLIDES_SANDALS)
        ],
        [
            InlineKeyboardButton(text='BASKETBALL', callback_data=BASKETBALL),
            InlineKeyboardButton(text='MOTOSPORT', callback_data=MOTOSPORT)
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

women_shoes_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='LIFESTYLE', callback_data=LIFESTYLE),
            InlineKeyboardButton(text='CLASSICS', callback_data=CLASSICS),
            InlineKeyboardButton(text='RUNNING', callback_data=RUNNING)
        ],
        [
            InlineKeyboardButton(text='TRAINING & GYM', callback_data=TRAINING_GYM),
            InlineKeyboardButton(text='SLIDES & SANDALS', callback_data=SLIDES_SANDALS)
        ],
        [
            InlineKeyboardButton(text='BASKETBALL PERFORMANCE', callback_data=BASKETBALL)
        ],
        [
            InlineKeyboardButton(text='BASKETBALL HERITAGE', callback_data=BASKETBALL)
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

mens_clothing_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='T-SHIRTS & TOPS', callback_data=T_SHIRTS_TOPS),
            InlineKeyboardButton(text='SHORTS', callback_data=SHORTS)

        ],
        [
            InlineKeyboardButton(text='SWEATSHIRTS & HOODIES', callback_data=SWEATSHIRTS_HOODIES)
        ],
        [
            InlineKeyboardButton(text='TRACKSUITS', callback_data=TRACKSUITS),
            InlineKeyboardButton(text='JACKETS', callback_data=JACKETS),
            InlineKeyboardButton(text='PANTS', callback_data=PANTS)
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

women_clothing_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='T-SHIRTS & TOPS', callback_data=T_SHIRTS_TOPS),
            InlineKeyboardButton(text='SHORTS', callback_data=SHORTS),
        ],
        [
            InlineKeyboardButton(text='SWEATSHIRTS & HOODIES', callback_data=SWEATSHIRTS_HOODIES)
        ],
        [
            InlineKeyboardButton(text='TRACKSUITS', callback_data=TRACKSUITS),
            InlineKeyboardButton(text='JACKETS', callback_data=JACKETS),
            InlineKeyboardButton(text='PANTS', callback_data=PANTS)
        ],
        [
            InlineKeyboardButton(text='LEGGINGS', callback_data=LEGGINGS),
            InlineKeyboardButton(text='SPORTS BRAS', callback_data=BRAS)
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_accessories = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 15 USD', callback_data='0.00,15.00'),
            InlineKeyboardButton(text=f'15 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 25 USD', callback_data='15.00,25.00'),
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 30 USD', callback_data='25.00,30.00')
        ],
        [
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 35 USD', callback_data='30.00, 35.00'),
            InlineKeyboardButton(text=emoji.emojize('35 :left_right_arrow: 40 USD', use_aliases=True), callback_data='35.00,40.00'),
            InlineKeyboardButton(text=emoji.emojize('40 :left_right_arrow: 50 USD', use_aliases=True), callback_data='40.00,50.00'),
        ],
        [
            InlineKeyboardButton(text=emoji.emojize('50 :left_right_arrow: 70 USD', use_aliases=True), callback_data='50.00,70.00'),
            InlineKeyboardButton(text=emoji.emojize('70 :left_right_arrow: 100 USD', use_aliases=True), callback_data='70.00,100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_kids_clothing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 25 USD', callback_data='0.00,25.00'),
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 35 USD', callback_data='25.00,35.00'),
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 45 USD', callback_data='35.00,45.00')
        ],
        [
            InlineKeyboardButton(text=f'45 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='45.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='60.00,80.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_kids_shoes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 25 USD', callback_data='0.00,25.00'),
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 30 USD', callback_data='25.00,30.00'),
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 35 USD', callback_data='30.00,35.00')
        ],
        [
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 40 USD', callback_data='35.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 45 USD', callback_data='40.00,45.00'),
            InlineKeyboardButton(text=f'45 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='45.00,50.00')

        ],
        [
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 55 USD', callback_data='50.00,55.00'),
            InlineKeyboardButton(text=f'55 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='55.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='60.00,80.00')
        ],
        [
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='80.00,100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_lifestyle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 35 USD', callback_data='0.00,35.00'),
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 40 USD', callback_data='35.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='40.00,50.00')
        ],
        [
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD',callback_data='50.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='70.00,80.00')
        ],
        [
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 90 USD', callback_data='80.00,90.00'),
            InlineKeyboardButton(text=f'90 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='90.00,120.00')
        ],
        [
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='120.00,150.00'),
            InlineKeyboardButton(text=f'150 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 200 USD', callback_data='150.00,200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_classics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 40 USD', callback_data='0.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='40.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00')
        ],
        [
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 75 USD', callback_data='60.00,75.00'),
            InlineKeyboardButton(text=f'75 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='75.00,120.00')
        ],
        [
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 200 USD', callback_data='120.00,200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_training = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 50 USD', callback_data='0.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00')
        ],
        [
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='70.00,80.00'),
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 90 USD', callback_data='80.00,90.00'),
            InlineKeyboardButton(text=f'90 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='90.00,120.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_running = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 50 USD', callback_data='0.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00')
        ],
        [
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 90 USD', callback_data='70.00,90.00'),
            InlineKeyboardButton(text=f'90 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='90.00,120.00')
        ],
        [
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='120.00,150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_slides = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 15 USD', callback_data='0.00,15.00'),
            InlineKeyboardButton(text=f'15 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 25 USD', callback_data='15.00,25.00'),
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='25.00,50.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_basketball_p = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 70 USD', callback_data='0.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 110 USD', callback_data='70.00,110.00')
        ],
        [
            InlineKeyboardButton(text=f'110 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 160 USD', callback_data='110.00,160.00'),
            InlineKeyboardButton(text=f'160 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 200 USD', callback_data='160.00,200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_basketball_h = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 50 USD', callback_data='0.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='50.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='70.00,80.00')
        ],
        [
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='80.00,100.00'),
            InlineKeyboardButton(text=f'100 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='100.00,120.00')
        ],
        [
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='120.00,150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_motosport = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 50 USD', callback_data='0.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='50.00,80.00'),
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='80.00,100.00')
        ],
        [
            InlineKeyboardButton(text=f'100 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 130 USD', callback_data='100.00,130.00'),
            InlineKeyboardButton(text=f'130 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 160 USD', callback_data='130.00,160.00')
        ],
        [
            InlineKeyboardButton(text=f'160 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 200 USD', callback_data='160.00,200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_tshirts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 15 USD', callback_data='0.00,15.00'),
            InlineKeyboardButton(text=f'15 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 20 USD', callback_data='15.00,20.00'),
            InlineKeyboardButton(text=f'20 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 30 USD', callback_data='20.00,30.00')
        ],
        [
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 35 USD', callback_data='30.00,35.00'),
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 40 USD', callback_data='35.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 45 USD', callback_data='40.00,45.00')
        ],
        [
            InlineKeyboardButton(text=f'45 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='45.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 55 USD', callback_data='50.00,55.00'),
            InlineKeyboardButton(text=f'55 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='55.00,60.00')
        ],
        [
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 80 USD', callback_data='70.00,80.00'),
            InlineKeyboardButton(text=f'80 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='80.00,100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_hoodies = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 30 USD', callback_data='0.00,30.00'),
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 40 USD', callback_data='30.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='40.00,50.00')
        ],
        [

            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='50.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 85 USD', callback_data='70.00,85.00'),
            InlineKeyboardButton(text=f'85 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='85.00,100.00')
        ],
        [
            InlineKeyboardButton(text=f'100 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='100.00,120.00'),
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='120.00,150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_shorts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 25 USD', callback_data='0.00,25.00'),
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 30 USD', callback_data='25.00,30.00'),
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 45 USD', callback_data='30.00,45.00')
        ],
        [
            InlineKeyboardButton(text=f'45 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='45.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00'),
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_tracksuits = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 35 USD', callback_data='0.00,35.00'),
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='35.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 60 USD', callback_data='50.00,60.00')
        ],
        [
            InlineKeyboardButton(text=f'60 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='60.00,70.00'),
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='70.00,100.00')
        ],
        [
            InlineKeyboardButton(text=f'100 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='100.00,150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_pants = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 30 USD', callback_data='0.00,30.00'),
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 45 USD', callback_data='30.00,45.00'),
            InlineKeyboardButton(text=f'45 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='45.00,70.00')
        ],
        [
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 85 USD', callback_data='70.00,85.00'),
            InlineKeyboardButton(text=f'85 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='85.00,120.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_leggings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 30 USD', callback_data='0.00,30.00'),
            InlineKeyboardButton(text=f'30 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='30.00,50.00')
        ],
        [
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 85 USD', callback_data='50.00,85.00'),
            InlineKeyboardButton(text=f'85 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='85.00,100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_bras = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 20 USD', callback_data='0.00,20.00'),
            InlineKeyboardButton(text=f'20 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 25 USD', callback_data='20.00,25.00')
        ],
        [
            InlineKeyboardButton(text=f'25 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 35 USD', callback_data='25.00,35.00'),
            InlineKeyboardButton(text=f'35 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='35.00,50.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_jackets = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='to 40 USD', callback_data='0.00,40.00'),
            InlineKeyboardButton(text=f'40 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 50 USD', callback_data='40.00,50.00'),
            InlineKeyboardButton(text=f'50 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 70 USD', callback_data='50.00,70.00')
        ],
        [
            InlineKeyboardButton(text=f'70 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 100 USD', callback_data='70.00,100.00'),
            InlineKeyboardButton(text=f'100 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 120 USD', callback_data='100.00,120.00')
        ],
        [
            InlineKeyboardButton(text=f'120 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 150 USD', callback_data='120.00,150.00'),
            InlineKeyboardButton(text=f'150 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 220 USD', callback_data='150.00,220.00')
        ],
        [
            InlineKeyboardButton(text=f'220 {emoji.emojize(":left_right_arrow:", use_aliases=True)} 250 USD', callback_data='220.00,250.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)
