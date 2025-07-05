from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "8093761224:AAHVf1sKf18PdGNy8Q1fpym4TpTqn04dHK4"
GROUP_CHAT_ID = -1001234567890

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🛒 Buy Subscription", callback_data="buy"),
        InlineKeyboardButton("🛠 Support", callback_data="support"),
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
        InlineKeyboardButton("⚙ Settings", callback_data="settings")
    )
    return kb

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Welcome to the mini app!", reply_markup=main_menu())

@dp.callback_query_handler(lambda c: c.data == "buy")
async def buy_handler(call: types.CallbackQuery):
    # Здесь будет логика выбора тарифа и оплаты
    await call.answer("Buy clicked")
    await call.message.edit_text("Choose subscription length:", reply_markup=subscription_menu())

def subscription_menu():
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(
        InlineKeyboardButton("7 days", callback_data="days_7"),
        InlineKeyboardButton("14 days", callback_data="days_14"),
        InlineKeyboardButton("30 days", callback_data="days_30"),
        InlineKeyboardButton("Back", callback_data="main")
    )
    return kb

@dp.callback_query_handler(lambda c: c.data == "main")
async def back_to_main(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("Welcome to the mini app!", reply_markup=main_menu())

# Добавим обработчик для тарифов и так далее...

if __name__ == "__main__":
    executor.start_polling(dp)
