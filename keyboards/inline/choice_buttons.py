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
            InlineKeyboardButton(text="MEN", callback_data=MEN),
            InlineKeyboardButton(text="WOMEN", callback_data=WOMEN),
            InlineKeyboardButton(text="BOYS", callback_data=KIDS_BOYS),
            InlineKeyboardButton(text="GIRLS", callback_data=KIDS_GIRLS)
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
            InlineKeyboardButton(text='BASKETBALL PERFORMANCE', callback_data=BASKETBALL_PERFORMANCE)
        ],
        [
            InlineKeyboardButton(text='BASKETBALL HERITAGE', callback_data=BASKETBALL_HERITAGE)
        ],
        [
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
            InlineKeyboardButton(text='BASKETBALL PERFORMANCE', callback_data=BASKETBALL_PERFORMANCE)
        ],
        [
            InlineKeyboardButton(text='BASKETBALL HERITAGE', callback_data=BASKETBALL_HERITAGE)
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
            InlineKeyboardButton(text='15 USD', callback_data='15.00'),
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='35 USD', callback_data='35.00')
        ],
        [
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='50 USD', callback_data='45.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_kids_clothing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='35 USD', callback_data='35.00'),
            InlineKeyboardButton(text='45 USD', callback_data='45.00')
        ],
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_kids_shoes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='35 USD', callback_data='35.00'),
            InlineKeyboardButton(text='40 USD', callback_data='40.00')
        ],
        [
            InlineKeyboardButton(text='45 USD', callback_data='45.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='55 USD', callback_data='55.00')
        ],
        [
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
        ]
    ]
)

choose_price_lifestyle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='35 USD', callback_data='35.00'),
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00')
        ],
        [
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00'),
            InlineKeyboardButton(text='90 USD', callback_data='90.00')
        ],
        [
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00'),
            InlineKeyboardButton(text='200 USD', callback_data='200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_classics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00')
        ],
        [
            InlineKeyboardButton(text='75 USD', callback_data='75.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='200 USD', callback_data='200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_training = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00')
        ],
        [
            InlineKeyboardButton(text='80 USD', callback_data='80.00'),
            InlineKeyboardButton(text='90 USD', callback_data='90.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_running = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00')
        ],
        [
            InlineKeyboardButton(text='90 USD', callback_data='90.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_slides = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='15 USD', callback_data='15.00'),
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_basketball_p = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='110 USD', callback_data='110.00'),
            InlineKeyboardButton(text='160 USD', callback_data='160.00'),
            InlineKeyboardButton(text='200 USD', callback_data='200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_basketball_h = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00')
        ],
        [
            InlineKeyboardButton(text='100 USD', callback_data='100.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_motosport = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text='130 USD', callback_data='130.00'),
            InlineKeyboardButton(text='160 USD', callback_data='160.00'),
            InlineKeyboardButton(text='200 USD', callback_data='200.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_tshirts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='15 USD', callback_data='15.00'),
            InlineKeyboardButton(text='20 USD', callback_data='20.00'),
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='35 USD', callback_data='35.00')
        ],
        [
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='45 USD', callback_data='45.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='55 USD', callback_data='55.00')
        ],
        [
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='80 USD', callback_data='80.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_hoodies = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00')
        ],
        [

            InlineKeyboardButton(text='85 USD', callback_data='85.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_shorts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='45 USD', callback_data='45.00')
        ],
        [
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_tracksuits = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='35 USD', callback_data='35.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='60 USD', callback_data='60.00')
        ],
        [
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_pants = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='45 USD', callback_data='45.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00')
        ],
        [
            InlineKeyboardButton(text='85 USD', callback_data='85.00'),
            InlineKeyboardButton(text='120 USD', callback_data='120.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_leggings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='30 USD', callback_data='30.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='85 USD', callback_data='85.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_bras = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='20 USD', callback_data='20.00'),
            InlineKeyboardButton(text='25 USD', callback_data='25.00'),
            InlineKeyboardButton(text='35 USD', callback_data='35.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_price_jackets = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='40 USD', callback_data='40.00'),
            InlineKeyboardButton(text='50 USD', callback_data='50.00'),
            InlineKeyboardButton(text='70 USD', callback_data='70.00'),
            InlineKeyboardButton(text='100 USD', callback_data='100.00')
        ],
        [
            InlineKeyboardButton(text='120 USD', callback_data='120.00'),
            InlineKeyboardButton(text='150 USD', callback_data='150.00'),
            InlineKeyboardButton(text='220 USD', callback_data='220.00'),
            InlineKeyboardButton(text='250 USD', callback_data='250.00')
        ],
        [
            InlineKeyboardButton(text=CANCEL, callback_data=PRICE_CANCEL)
        ]
    ]
)

choose_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='next 10', callback_data='next')
        ]
    ]
)
