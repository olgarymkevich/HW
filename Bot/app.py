import telebot
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    text = "Привет! Я Бот-Конвертер валют и я могу:\n- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты через команду <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
- Напомнить, что я могу, через команду /help"
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def send_welcome(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n- Показать список доступных валют через команду /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise APIException('Слишком много параметров.')
        elif len(values) < 3:
            raise APIException('Слишком мало параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()