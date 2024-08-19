from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Замените 'YOUR_API_TOKEN' на токен вашего бота, который вы получили от BotFather
TOKEN = '7534914673:AAEj3mkx-rUwBUPNWGPGr7rwP5BNktuWgm4'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /start."""
    await update.message.reply_text('Привет! Я ваш бот. Используйте команду /help для получения помощи.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /help."""
    await update.message.reply_text('Команды:\n/start - Начать разговор\n/help - Помощь\n/get - список питомцев')

def main() -> None:
    """Запускает бота."""
    # Создаем объект `Application` и передаем ему токен вашего бота
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
