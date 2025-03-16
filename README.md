EN:
Telegram Bot Instruction Manual
This document provides a comprehensive guide on how to use the Telegram bot created by BorFather. The bot is designed to interact with users, provide assistance, and answer questions using OpenAI's API via OpenRouter. Below, you will find detailed instructions on how to set up, configure, and use the bot.

Table of Contents
Introduction

Prerequisites

Setting Up the Bot

3.1. Obtain Telegram Bot Token

3.2. Obtain OpenRouter API Key

3.3. Install Required Libraries

3.4. Configure Environment Variables

Running the Bot

Bot Commands and Features

5.1. /start Command

5.2. /search Command

5.3. /help Command

5.4. Inline Buttons

5.5. Text Message Handling

Troubleshooting

Conclusion

1. Introduction
The Telegram bot is a conversational AI assistant that leverages OpenAI's GPT model via OpenRouter to provide answers to user queries. It supports both text-based interactions and button-based navigation for ease of use. The bot is designed to be simple, intuitive, and efficient.

2. Prerequisites
Before using the bot, ensure you have the following:

A Telegram account.

A Telegram bot token (obtained from BotFather).

An OpenRouter API key (sign up at OpenRouter).

Python 3.7 or higher installed on your system.

Basic knowledge of running Python scripts.

3. Setting Up the Bot
3.1. Obtain Telegram Bot Token
Open Telegram and search for BotFather.

Start a chat with BotFather and use the /newbot command.

Follow the instructions to create a new bot. BotFather will provide you with a bot token. Save this token securely.

3.2. Obtain OpenRouter API Key
Go to OpenRouter and sign up for an account.

Navigate to the API Keys section and generate a new API key.

Save the API key securely.

3.3. Install Required Libraries
Install the necessary Python libraries using pip:

bash
Copy
pip install python-telegram-bot openai python-dotenv
3.4. Configure Environment Variables
Create a .env file in the same directory as your bot script.

Add the following lines to the .env file:

plaintext
Copy
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
Replace your_telegram_bot_token and your_openrouter_api_key with the actual values.

4. Running the Bot
Save the bot script provided by BorFather in a file (e.g., bot.py).

Run the script using Python:

bash
Copy
python bot.py
The bot will start and begin listening for messages. You can now interact with it on Telegram.

5. Bot Commands and Features
5.1. /start Command
Purpose: Initializes the bot and displays a welcome message.

Usage: Type /start in the chat.

Behavior:

Displays a welcome message.

Shows a Reply Keyboard with buttons for "Search" and "Help".

Displays Inline Buttons for "Search" and "Help".

5.2. /search Command
Purpose: Prompts the user to enter a question for the bot to answer.

Usage: Type /search in the chat.

Behavior:

Asks the user to input their question.

Sends the question to OpenAI via OpenRouter and displays the response.

5.3. /help Command
Purpose: Displays a list of available commands and their descriptions.

Usage: Type /help in the chat.

Behavior:

Lists the following commands:

/start - Start the bot.

/search - Ask a question.

/help - Show all commands.

5.4. Inline Buttons
Purpose: Provides quick access to common actions without typing commands.

Usage: Click on the inline buttons displayed after using /start.

Behavior:

Search Button: Prompts the user to enter a question.

Help Button: Displays the help message.

5.5. Text Message Handling
Purpose: Allows the bot to process free-form text messages.

Usage: Type any message in the chat (e.g., "What is the capital of France?").

Behavior:

If the message is "Search" or "Help", the bot responds accordingly.

For other messages, the bot sends the text to OpenAI via OpenRouter and replies with the generated response.

6. Troubleshooting
Bot Not Responding:

Ensure the bot is running and the script has no errors.

Check your internet connection.

Verify that the Telegram bot token and OpenRouter API key are correct.

API Errors:

If the bot fails to fetch a response, check the logs for errors.

Ensure your OpenRouter API key is valid and has sufficient credits.

Environment Variables Not Loaded:

Ensure the .env file is in the same directory as the script.

Verify the variable names in the .env file match those in the script.

Button Issues:

If inline buttons do not work, ensure the CallbackQueryHandler is properly registered in the script.

7. Conclusion
This Telegram bot is a powerful tool for answering questions and providing assistance using AI. By following this guide, you can set up, configure, and use the bot effectively. If you encounter any issues, refer to the troubleshooting section or reach out to BorFather for support.

Enjoy using your AI-powered Telegram bot! 🚀

Note: This bot is designed for educational and personal use. Ensure compliance with OpenAI's and Telegram's terms of service when deploying it in production environments.


RU:
Руководство по использованию Telegram-бота
Этот документ представляет собой подробное руководство по использованию Telegram-бота, созданного BorFather. Бот предназначен для взаимодействия с пользователями, предоставления помощи и ответов на вопросы с использованием OpenAI API через OpenRouter. Ниже вы найдете пошаговые инструкции по настройке, конфигурации и использованию бота.

Содержание
Введение

Необходимые условия

Настройка бота

3.1. Получение токена Telegram-бота

3.2. Получение API-ключа OpenRouter

3.3. Установка необходимых библиотек

3.4. Настройка переменных окружения

Запуск бота

Команды и функции бота

5.1. Команда /start

5.2. Команда /search

5.3. Команда /help

5.4. Inline-кнопки

5.5. Обработка текстовых сообщений

Устранение неполадок

Заключение

1. Введение
Telegram-бот — это AI-ассистент, который использует модель GPT от OpenAI через OpenRouter для ответов на вопросы пользователей. Бот поддерживает как текстовые взаимодействия, так и навигацию с помощью кнопок для удобства использования. Он прост, интуитивно понятен и эффективен.

2. Необходимые условия
Перед использованием бота убедитесь, что у вас есть следующее:

Аккаунт в Telegram.

Токен Telegram-бота (полученный от BotFather).

API-ключ OpenRouter (зарегистрируйтесь на OpenRouter).

Python 3.7 или выше, установленный на вашем устройстве.

Базовые знания по запуску Python-скриптов.

3. Настройка бота
3.1. Получение токена Telegram-бота
Откройте Telegram и найдите BotFather.

Начните чат с BotFather и используйте команду /newbot.

Следуйте инструкциям, чтобы создать нового бота. BotFather предоставит вам токен бота. Сохраните этот токен в надежном месте.

3.2. Получение API-ключа OpenRouter
Перейдите на сайт OpenRouter и зарегистрируйте аккаунт.

Перейдите в раздел API Keys и создайте новый API-ключ.

Сохраните API-ключ в надежном месте.

3.3. Установка необходимых библиотек
Установите необходимые библиотеки с помощью pip:

bash
Copy
pip install python-telegram-bot openai python-dotenv
3.4. Настройка переменных окружения
Создайте файл .env в той же директории, где находится ваш скрипт бота.

Добавьте следующие строки в файл .env:

plaintext
Copy
TELEGRAM_BOT_TOKEN=ваш_токен_бота
OPENROUTER_API_KEY=ваш_api_ключ_openrouter
Замените ваш_токен_бота и ваш_api_ключ_openrouter на реальные значения.

4. Запуск бота
Сохраните скрипт бота, предоставленный BorFather, в файл (например, bot.py).

Запустите скрипт с помощью Python:

bash
Copy
python bot.py
Бот начнет работать и будет ожидать сообщений. Теперь вы можете взаимодействовать с ним в Telegram.

5. Команды и функции бота
5.1. Команда /start
Назначение: Инициализирует бота и отображает приветственное сообщение.

Использование: Введите /start в чате.

Поведение:

Отображает приветственное сообщение.

Показывает Reply Keyboard с кнопками "Поиск" и "Помощь".

Отображает Inline-кнопки для "Поиск" и "Помощь".

5.2. Команда /search
Назначение: Предлагает пользователю ввести вопрос для получения ответа.

Использование: Введите /search в чате.

Поведение:

Просит пользователя ввести вопрос.

Отправляет вопрос в OpenAI через OpenRouter и отображает ответ.

5.3. Команда /help
Назначение: Отображает список доступных команд и их описание.

Использование: Введите /help в чате.

Поведение:

Перечисляет следующие команды:

/start — Запустить бота.

/search — Задать вопрос.

/help — Показать все команды.

5.4. Inline-кнопки
Назначение: Предоставляет быстрый доступ к часто используемым действиям без ввода команд.

Использование: Нажмите на inline-кнопки, отображаемые после использования /start.

Поведение:

Кнопка "Поиск": Предлагает пользователю ввести вопрос.

Кнопка "Помощь": Отображает сообщение с помощью.

5.5. Обработка текстовых сообщений
Назначение: Позволяет боту обрабатывать произвольные текстовые сообщения.

Использование: Введите любое сообщение в чате (например, "Какая столица Франции?").

Поведение:

Если сообщение — "Поиск" или "Помощь", бот отвечает соответствующим образом.

Для других сообщений бот отправляет текст в OpenAI через OpenRouter и отвечает сгенерированным ответом.

6. Устранение неполадок
Бот не отвечает:

Убедитесь, что бот запущен и в скрипте нет ошибок.

Проверьте подключение к интернету.

Убедитесь, что токен Telegram-бота и API-ключ OpenRouter указаны правильно.

Ошибки API:

Если бот не может получить ответ, проверьте логи на наличие ошибок.

Убедитесь, что ваш API-ключ OpenRouter действителен и имеет достаточный баланс.

Переменные окружения не загружены:

Убедитесь, что файл .env находится в той же директории, что и скрипт.

Проверьте, что имена переменных в файле .env совпадают с теми, что используются в скрипте.

Проблемы с кнопками:

Если inline-кнопки не работают, убедитесь, что CallbackQueryHandler правильно зарегистрирован в скрипте.

7. Заключение
Этот Telegram-бот — мощный инструмент для ответов на вопросы и предоставления помощи с использованием искусственного интеллекта. Следуя этому руководству, вы сможете настроить, сконфигурировать и эффективно использовать бота. Если возникнут проблемы, обратитесь к разделу по устранению неполадок или свяжитесь с BorFather для получения поддержки.

Наслаждайтесь использованием вашего AI-бота! 🚀

Примечание: Этот бот предназначен для образовательных и личных целей. При использовании в производственных средах убедитесь в соблюдении условий использования OpenAI и Telegram.
