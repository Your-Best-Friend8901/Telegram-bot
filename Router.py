
from aiogram import Router,F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import callback_data,CommandStart
from buttons import keyboard
from inlinekeyaborad import inline_kb,inline_kb1
from aiogram.fsm.context import FSMContext


message_handler = Router()

@message_handler.message(CommandStart())
async def message_handler0(message:Message):
    await message.answer('Ваш меню открыт:',reply_markup=keyboard)
@message_handler.message(F.text =='✨💎 𝓖𝓮𝓶 𝓢𝓽𝓸𝓻𝓮 💎✨')
async def message_handler1(message:Message):
    await message.answer('✨💎Основные пакеты покупки гемов💎✨',reply_markup=inline_kb)
@message_handler.message(F.text =='🌟📚 𝓐𝓫𝓸𝓾𝓽 𝓤𝓼 📚🌟')
async def message_handler2(message:Message):
    await message.answer('''Привет! 👋
Этот бот создан для практики и учебных целей.
Его разработал Анвар — человек, который любит программировать и учиться новому.
Рад помочь тебе и надеюсь, что бот будет полезным!''')
@message_handler.message(F.text =='🛒 𝓒𝓪𝓻𝓽 🛒')
async def message_handler3(message:Message,state:FSMContext):
    try:
        data =await state.get_data()
        rub = data['total_gems']*6.67
        dollar = rub/79.07
        await state.update_data(Dollar=dollar)
        await message.answer(f"""🛒 Ваша корзина:
        В ней сейчас находится {data['total_gems']} гемов💎 
        Результат:{data['total_gems']*6.67}₽🔥
        Результат:${dollar:.2f}🔥""",reply_markup=inline_kb1)

    except KeyError:
        await message.answer("""🛒 Ваша корзина:
        В ней сейчас находится 0 гемов💎""")
@message_handler.message(F.text =='🚪 𝓔𝔁𝓲𝓽 🚪')
async def message_handler4(message:Message):
    await message.answer('Вы вышли с меню🚪',reply_markup=ReplyKeyboardRemove())

