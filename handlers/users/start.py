from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from states.state import MainState
from keyboards.default.main_buttons import *


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    name = message.from_user.username
    user = db.select_user(id=message.from_user.id)

    if user is None:
        user = db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
        )
        count = db.count_users()
        msg = f"@[{message.from_user.full_name}](tg://user?id={message.from_user.id}) " \
              f"bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg, parse_mode='markdown')
    await bot.send_message(chat_id=ADMINS[0], text=f'@{name} bazaga oldin qo\'shilgan')
    answer = f"Assalomu alaykum [{message.from_user.full_name}](tg://user?id={message.from_user.id}) ! \n" \
             f"Men sizni UzBCoder bilan bog'lovchi botman, men bilan muloqot qilish uchun tugmalardan foydalaning."
    await message.answer(answer, parse_mode="markdown", reply_markup=main)
    await MainState.command.set()
