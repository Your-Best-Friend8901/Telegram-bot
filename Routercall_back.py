from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from inlinekeyaborad import keyboard2


call_back = Router()

class Form(StatesGroup):
    Gems = State()

@call_back.callback_query(F.data.in_(['30','250','500','1200','2500']))
async def message_handler_callback0(callback:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    total_gems =data.get('total_gems',0)
    total_gems += int(callback.data)
    await state.update_data(total_gems=total_gems)
    await callback.message.answer(f'Отлично! Ваша корзина пополнена — теперь там {total_gems} гемов 💎')

@call_back.callback_query(F.data =='clear')
async def message_handler_callback1(callback:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    total_gems = data.get('total_gems')
    total_gems = 0
    await state.update_data(total_gems=total_gems)
    await callback.message.answer('Ваша корзина была успешно очищена! 🧹✅')

@call_back.callback_query(F.data =='buy')
async def message_handler_callback2(callback:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    total_gems = data.get('total_gems',0)
    if total_gems == 0:
        await callback.message.answer('''🛒 Корзина выглядит грустно… Пора её порадовать! Закинь что-нибудь, и мы сразу откроем оплату 💳''')
    else:
        await callback.message.answer(f'''🎉 Поддерживаем удобные способы оплаты!
        
    🔐 Криптовалюта через CryptoBot - Оплачивай в USDT, BTC, ETH и других популярных монетах — удобно и без лишних вопросов
    
    💳 Банковская карта через Tinkoff - Оплата напрямую с карты''',reply_markup=keyboard2)


