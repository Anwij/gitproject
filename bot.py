import telebot
import requests
import django
from time import sleep

url = r'https://api.telegram.org/bot637861645:AAEYDWviuBn8KpSDp6Un_copMZTeevecDFw/'
token = '637861645:AAEYDWviuBn8KpSDp6Un_copMZTeevecDFw'


def get_updates_json(request):
	#params = {'timeout': 100, 'offset': None}
	#response = requests.get(request + 'getUpdates', data=params)
	response = requests.get(request + 'getUpdates')
	return response.json()
	
def last_update(data):
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]

def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id
	
def send_mess(chat, text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

#chat_id = get_chat_id(last_update(get_updates_json(url)))

#send_mess(chat_id, 'Sosi pisos')


def main():
	a = 0
	bot = telebot.TeleBot(token)
	bot.send_message(get_chat_id(last_update(get_updates_json(url))), 
			'hello')
	update_id = last_update(get_updates_json(url))['update_id']
	
	while True:
		'''
		var = last_update(get_updates_json(url))['update_id'] 
		if update_id <= var:
			update_id = var + 1
			send_mess(get_chat_id(last_update(get_updates_json(
					url))),	var)
		
		bot.send_message(get_chat_id(last_update(get_updates_json(url))), 
			'hello' + str(a))
		a += 1
		'''
		sleep(3)
	
if __name__ == '__main__':
	main()
