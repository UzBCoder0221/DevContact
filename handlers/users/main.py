import asyncio
from datetime import datetime
from aiogram import types
from loader import bot, db, dp
from data.config import *
from states.state import *
from keyboards.default.main_buttons import *
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=["menu"], state='*')
async def start(message: types.Message):
    await message.answer("Bosh menu", reply_markup=main)


@dp.message_handler(state=MainState.command)
async def send_message(message: types.Message):
    msg = message.text
    if msg == "📝 UzBCoder ga rasmiy xabar yuborish":
        answer = f"UzBCoder ga murojaat qilishingiz uchun siz:\n\n" \
                 f"• Shaxsingizni yashirmasligingiz (asl ismingiz nazarda tutilmoqda)\n\n" \
                 f"• Ish joyingizni ma'lumotlari (qayerda ishlashingiz, bu ish haqqimiz uchun muhim)\n\n" \
                 f"• Yozganlaringiz aniq va tushinarli bo'lishi (sizning loyihangizni tushinishimiz uchun)\n\n" \
                 f"\n\n\n <b>Diqqat hurmatli mijoz</b> ❗️❗️❗️\n\n" \
                 f"<b><i>• Loyihangizni bizga buyurtma berishdan oldin yaxshilab o'ylab ko'ring, o'zingiz " \
                 f"tushinmagan narsani yasashni aytib bizning vaqtimizni olmang ️ !\n\n" \
                 f"• Loyiga buyurtma berganingizda ikki tomonlama online shartnoma tuziladi," \
                 f"sizning telefon raqamingiz, yashash manzilingiz, joiz bo'lgan hollarda passportingiz dagi " \
                 f"ma'lumotlar so'raladi. Bu bizni vaqtimizni zoya ketkazmasligingiz uchun va siz bilan " \
                 f"bog'lanishimiz uchun zarur.\n\n" \
                 f"• Loyihaga buyurtma berganingizdan so'ng 48 soat ichida bekor qilish huquqiga ega bo'lasiz. 48 soatdan " \
                 f"keyin esa shartona tuzilganligi va bizni dasturlash uchun sarflangan (bekor ketgan) vaqtimizni " \
                 f"moddiy tomonlama qoplash uchun, kelishilgan summaning buyurtma berilgan kundan 48 soat o'tgandan keyin, " \
                 f"yana 3 kun ichida bekor qilinsa 10%, 5 kun ichida 15%, 7 kun ichida 30%, 14 kungacha 50%, 14 kundan ko'p " \
                 f"kunlar o'tgan hollarda 70% dan 90% gacha, loyihangiz 30% - 70% oralig'ida tugallangan holda summaning 60%, " \
                 f"70%-90% oralig'ida tugallangan bo'lsa summaning 70% i dan 90% i gacha jarima to'lovi to'lanadi.\n\n" \
                 f"• Ikki tomonlama shartnoma shartlariga amal qilinmagan holda va jarima to'lovi to'lanilmagan " \
                 f"(firibgarlik) hollarda mazkur ikki tomonlama shartnoma bo'yicha shahar(cha) sudiga murojaat qilinadi " \
                 f"va ikki tomon maanfatlari qondiriladi.</i></b>\n\nHurmatli foydalanuvchi hammasi tushunarli bo'ldi degan " \
                 f"umiddaman."
        await message.answer(answer, reply_markup=ok)
        await MainState.next()
    elif msg == "ℹ️ Bot haqida":
        answer = f"Bot nomi: {bot.get_me()}\n" \
                 f"Bot ishga tushurilgan sana: {datetime.today()}\n" \
                 f"Bot yaratuvchisi (egasi): UzBCoder\n" \
                 f"Yaratilgan tili: 🐍Python"
        await message.answer(answer)
    elif msg == "🌐 UzBCoder portfolio":
        await message.answer("ok")
    elif msg == "ℹ️ UzBCoder haqida":
        answer = f"Dasturlovchi taxallusi: <b><i>UzBCoder</i></b>\n" \
                 f"Dasturlovchi yoshi: 16 yosh\n" \
                 f"Dasturlashdagi tajribasi:\n" \
                 f"• Python (Web dasturlash, Back-End, Telegram Bot) 6+ oy, o'rganilgan asosiy kutibxonalari Django, " \
                 f"Aiogram, Pyrogram (hozirda bu kutubxonaga asoslangan loyihalar buyurtma berish mumkin emas).\n" \
                 f"• Java (Android Dasturlash) 1+ yil, katta loyihalar bilan va kurslarsiz o'rganilganligi sababli " \
                 f"hozirda kichik buyurtmalar berishingiz mumkin.\n" \
                 f"• Web Front-End (CSS, HTML, JS) kursda o'rganilmaganligi tufayli katta saytlar loyihalari " \
                 f"qabul qilinmaydi.\n" \
                 f"• PostgresSQL (database) lar bilan ishlash tajribasi 3+ oy. SQL emas PosgreSQL ikkisi bir emas " \
                 f"o'xshaganligi bilan.\n" \
                 f"• C, C++, C#, PHP, SQL kabi tillarda fundamental bilimlar (faqat o'rganilgan paytdagi dasturlar yasalgan)" \
                 f", faqat oddiy dasturlarga buyurtma berishingiz mumkin (kutubxonalar o'rganilmagan)."
        await message.answer(answer)
    else:
        await message.answer("Iltimos menga tugmalar yordamida xabar yuboring !")
    await asyncio.sleep(0.05)


@dp.message_handler(state=MainState.next_com)
async def send_message(message: types.Message):
    if message.text == "Hammasi tushunarli va bu shartlarga rozilik bildiraman":
        answer = "Yaxshi unday bo'lsa murojaat (muammo, loyiha, taklif va hokozo)laringizni 1 ta xabarda yozib yuboring " \
                 "yoki fayl sifatida menga yuboring, men uni UzBCoderga yetkazman."
        await message.answer(text=answer, reply_markup=ReplyKeyboardRemove())
        await MainState.next()
    else:
        await message.answer("Iltimos menga tugmalar yordamida xabar yuboring !")
    await asyncio.sleep(0.05)


@dp.message_handler(content_types=["any"], state=MainState.mess)
async def appeal(message: types.Message):
    await bot.copy_message(chat_id=ADMINS[0], from_chat_id=message.from_user.id, message_id=message.message_id)
    await bot.send_message(
        chat_id=ADMINS[0], text=f"{datetime.today()} \n\n [{message.from_user.full_name}]"
                                f"(tg://user?id={message.from_user.id})",
        parse_mode="markdown")
    await message.answer("Xabaringiz UzBCoder ga yuborildi ✅", reply_markup=main)
    await MainState.command.set()
    await asyncio.sleep(0.05)


@dp.message_handler(content_types=["any"])
async def files(message: types.Message):
    await message.answer("Iltimos menga tugmalar yordamida xabar yuboring !")
    await MainState.command.set()
    await asyncio.sleep(0.05)
