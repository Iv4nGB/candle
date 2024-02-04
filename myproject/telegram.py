import requests
TOKEN = "6380594023:AAEE2LT3trZR6mydrPCX0Djyd0COs-v9QwU"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())

chat_id = '5401729924'
message = "Привет, Иван"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json())
