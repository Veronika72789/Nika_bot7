import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Список шуток
jokes = [
    "Дантэс на Поле чудес - прощайте барабан!",
    "Какую песню нельзя петь на кладбище? - Забери меня с собой.",
    "Крошка-картошка - организация, запрещённая в Беларуси.",
    "Охота - это спорт. Особенно когда патроны закончились, а кабан жив.",
    "Ты сейчас на удалёнке? Хуже. Я на увольнёнке."
]

# Функция для отправки шутки
async def tell_joke(update: Update, context):
    joke = random.choice(jokes)
    await update.message.reply_text(joke)

# Основной блок программы
if __name__ == "__main__":
    TELEGRAM_TOKEN = "7466094617:AAGU9k89bokdAGA9UcUo-NQ6WbZnfikQJ6M"
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Обработчик команды /joke
    app.add_handler(CommandHandler("joke", tell_joke))

    print("Хочешь шутку? Напиши /joke")
    app.run_polling()

