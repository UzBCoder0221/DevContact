from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main.add("📝 UzBCoder ga rasmiy xabar yuborish")
main.row("ℹ️ UzBCoder haqida", "ℹ️ Bot haqida")
main.add("🌐 UzBCoder portfolio")

ok = ReplyKeyboardMarkup([[KeyboardButton("Hammasi tushunarli va bu shartlarga rozilik bildiraman")]],
                         resize_keyboard=True, one_time_keyboard=True)
