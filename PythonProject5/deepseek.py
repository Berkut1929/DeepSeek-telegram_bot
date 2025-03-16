import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from openai import OpenAI

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация клиента OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="OpenRouter_API",  # Ваш API-ключ OpenRouter
)

def start(update: Update, context: CallbackContext) -> None:
    # Создаем Reply кнопки
    reply_keyboard = [
        [KeyboardButton("Поиск")],
        [KeyboardButton("Помощь")]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Привет! Выбери действие:', reply_markup=reply_markup)

    # Создаем Inline кнопки
    inline_keyboard = [
        [InlineKeyboardButton("Поиск", callback_data='inline_search')],
        [InlineKeyboardButton("Помощь", callback_data='inline_help')]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)
    update.message.reply_text('Или используй кнопки:', reply_markup=inline_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    if user_message == "Поиск":
        update.message.reply_text("Чем я могу помочь? Введите ваш вопрос.")
    elif user_message == "Помощь":
        show_help(update)
    else:
        # Отправляем сообщение "Подождите, это займет некоторое время"
        update.message.reply_text("Подождите, это займет некоторое время...")
        process_ai_request(update, user_message)

def process_ai_request(update: Update, user_message: str) -> None:
    try:
        # Отправка запроса к API
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[{"role": "user", "content": user_message}]
        )

        # Проверка и вывод ответа
        if completion.choices and len(completion.choices) > 0:
            response = completion.choices[0].message.content
            update.message.reply_text(response)
        else:
            update.message.reply_text("Извините, я не нашел ответа.")

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        update.message.reply_text("Произошла ошибка, попробуйте позже.")

def show_help(update: Update) -> None:
    commands = [
        "/start - Начать работу с ботом",
        "/search - Задать вопрос",
        "/help - Показать все команды"
    ]
    update.message.reply_text("\n".join(commands))

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'inline_search':
        query.edit_message_text(text="Чем я могу помочь? Введите ваш вопрос.")
    elif query.data == 'inline_help':
        show_help(query)

def search_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Чем я могу помочь? Введите ваш вопрос.")

def help_command(update: Update, context: CallbackContext) -> None:
    show_help(update)

def main() -> None:
    # Создаем Updater и передаём ему токен вашего бота
    updater = Updater("TELEGRAM_BOT_TOKEN")  # Ваш токен Telegram бота

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search_command))
    dp.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Регистрируем обработчик нажатий на Inline кнопки
    dp.add_handler(CallbackQueryHandler(button_handler))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")