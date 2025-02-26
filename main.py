import telebot
import numexpr

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

#/start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Введи математическое выражение, которое хочешь посчитать.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "это раздел о помощи! "
        '/start - запуск бота, /help - помощь.' )
    bot.reply_to(message,'Разрешенные знаки ( +, -, *, /, **(степень)')


@bot.message_handler(func=lambda message: True)
def handle_math_expression(message):
    try:

        result = numexpr.evaluate(message.text)
        bot.reply_to(message, f'Результат: {message.text} = {result}')
    except Exception as e:
        bot.reply_to(message, f'Произошла ошибка при вычислении: {e}')

if __name__ == "__main__":
    bot.polling()
