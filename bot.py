import telebot
import text
from re import match

token = '637861645:AAEYDWviuBn8KpSDp6Un_copMZTeevecDFw'
bot = telebot.TeleBot(token)
markup = telebot.types.ReplyKeyboardMarkup()
markup.row('Прайс')
markup.row('Работа', 'Информация')
markup.row('Оплатил "получить товар"', 'Отмена заказа')
druglist = {'amf': [('1г', 1200), ('3г', 2700),
			        ('5г', 4000), ('10г', 6500)],
            'hashish': [('1г', 700), ('3г', 1800),
			            ('5г', 2500), ('10г', 4500)],
            'lsd': [('1шт', 700), ('3шт', 1800),
			            ('5шт', 2500), ('10шт', 4500)],
			'mdma': [('1шт', 1000), ('3шт', 2100),
			            ('5шт', 3000), ('10шт', 5000)]}


@bot.message_handler(content_types=['text'])
def getMessageText(message):
	mText = message.text
	if mText == r'/start':
		answer = text.start
	elif mText == 'Прайс':
		answer = text.price
	elif mText == 'Информация':
		answer = text.info
	elif mText == 'Работа':
		answer = text.work
	elif mText == 'Оплатил "получить товар"':
		answer = text.goods
	elif mText == 'Отмена заказа':
		answer = text.cancel
	else:
		var = match(r'/[a-z]+\d', mText).group(0)[1:]
		drug = var[:-1]
		mass = var[-1]
		#if drug == 'amf':
			#answer = reserved.format
		answer = text.off
	bot.send_message(message.chat.id, answer, reply_markup=markup)	
	
if __name__ == '__main__':
	bot.polling(none_stop=True)
