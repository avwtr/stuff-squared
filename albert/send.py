import os
from twilio.rest import Client
from dotenv import load_dotenv
from facts_eng import facts

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
        body= <message>,
        from_= <number>,
         #replace with your own number 
        to= <recipient_num>
    )

print(message.sid)
