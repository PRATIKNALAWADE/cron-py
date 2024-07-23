import requests
from twillio_connection import set_twilio_connection,send_whatsapp_text


def get_QOD(category):
    url = "https://quotes.rest/qod?language=en&category={}".format(category)
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer API key"
                }
    res = requests.get(url=url,headers=headers)
    data = res.json()
    
    quote = data['contents']['quotes'][0]['quote']
    return quote

quote = get_QOD(category="inspire")
print(quote)
    
client = set_twilio_connection()

text = send_whatsapp_text(client,quote)
    
