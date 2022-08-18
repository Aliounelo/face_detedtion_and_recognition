import telegram
import requests

TELEGRAM_BOT_TOKEN = '5535933470:AAFWP__W6-1fAxqrCQbE2QTXFDygnZhFnN8'
TELEGRAM_CHAT_ID = '-696427975'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

#bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Telegram Bot")
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=926c0917bf5e42fda8e40569e5c796fb")
char = response.content.decode('utf-8')

info = ["ip_address", "city", "country","country_code","continent","longitude","latitude","connection","autonomous_system_organization","connection_type","isp_name","organization_name"]


text = ""
for i in char.split(',') :
    if i.split(':')[0].strip("{\"\"\"") in info :
        line = str(i.split(':')[0].strip("{\"\"\"")) + " : " + str(i.split(':')[1].strip("{\"\"\"}")) + "\n"
        text+=line

print(text)


#bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb')) 