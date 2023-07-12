from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from states.state import MainState
from keyboards.default.main_buttons import *


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    name = message.from_user.username
    user = await db.select_user(telegram_id=message.from_user.id)
    if user is None:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        count = await db.count_users()
        msg = f"@{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    await bot.send_message(chat_id=ADMINS[0], text=f'@{name} bazaga oldin qo\'shilgan')
    answer = f"Assalomu alaykum [{message.from_user.full_name}](tg://user?id={message.from_user.id}) ! \n" \
             f"Men sizni UzBCoder bilan bog'lovchi botman men bilan muloqot qilish uchun tugmalardan foydalaning."
    await message.answer(answer, parse_mode="markdown", reply_markup=main)
    await MainState.command.set()
