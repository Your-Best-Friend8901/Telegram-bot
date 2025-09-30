from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

b0=KeyboardButton(text='✨💎 𝓖𝓮𝓶 𝓢𝓽𝓸𝓻𝓮 💎✨')
b1=KeyboardButton(text='🌟📚 𝓐𝓫𝓸𝓾𝓽 𝓤𝓼 📚🌟')
b2=KeyboardButton(text='🛒 𝓒𝓪𝓻𝓽 🛒')
b3=KeyboardButton(text='🚪 𝓔𝔁𝓲𝓽 🚪')

buttons = [[b0],[b1],[b2,b3]]

keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True

)
