from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv(account_sid)
auth_token = os.getenv(auth_token)

phone_number = 123456

def set_twilio_connection():
    client = Client(account_sid, auth_token)
    return client
    
    
set_twilio_connection()    


def send_whatsapp_text(client,quote):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=quote,
    to='whatsapp:+91123456780')
    return (message.sid)
    
    