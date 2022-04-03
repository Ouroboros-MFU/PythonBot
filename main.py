import telebot
import random

# def secure(ans):
#     if ans.lower() in ['y', 'д']:
#         return True
#     else:
#         return False

answers = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова',	'Даже не думай',
'Предрешено', 	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет',
'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать', 'По моим данным - нет',
'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

bot = telebot.TeleBot('5155553013:AAGewhjGjrnS-zVbDk9QtgguBgqCvnBMpsg')    # подключение бота через токен

@bot.message_handler(content_types = ['text'])
def getMessage(message):
    print(message, message.text, sep='\n')

    if (message.text.lower() == "/start"):
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}, я магический шар, и я знаю ответ на любой твой вопрос.")
        bot.send_message(message.from_user.id, "Задай свой вопрос и я дам тебе ответ)")
    if (message.text.lower() != "/start"):
        bot.send_message(message.from_user.id, random.choice(answers))
    #else:
    #    bot.send_message(message.from_user.id, 'Я тебя не понимаю, пиши "/help"')



bot.polling(none_stop=True, interval=0) # мониторинг новых сообщений


