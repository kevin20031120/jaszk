import requests

x = "Hello"
y = "Hi"

r = requests.post('https://api.telegram.org/bot2017942575:AAFpsjlJlbzyG8DOZhdYZV6ugalmBke0RGU/sendMessage?chat_id=-517589081&text=%s'  % y)