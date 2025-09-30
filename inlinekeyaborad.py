from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
b0 = InlineKeyboardButton(text='💎 30 гемов',callback_data='30')
b1 = InlineKeyboardButton(text='💎 250 гемов',callback_data='250')
b2 = InlineKeyboardButton(text='💎 500 гемов',callback_data='500')
b3 = InlineKeyboardButton(text='💎 1,200 гемов',callback_data='1200')
b4 = InlineKeyboardButton(text='💎 2,500 гемов',callback_data='2500')

buttons = [[b0,b1],[b2,b3],[b4]]

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=buttons
)

b0 = InlineKeyboardButton(text='💳 Заплатить ✅',callback_data='buy')
b1 = InlineKeyboardButton(text='🗑️ Очистить корзину ♻️',callback_data='clear')

buttons = [[b0,b1]]

inline_kb1 =InlineKeyboardMarkup(
    inline_keyboard=buttons
)

b0 = InlineKeyboardButton(text='🔐 Криптовалюта',callback_data='Crypto_buy')
b1 = InlineKeyboardButton(text='💳 Банковская карта',callback_data='Cart_buy')

buttons=[[b0,b1]]

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=buttons
)