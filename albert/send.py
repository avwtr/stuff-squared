import os
from twilio.rest import Client
from dotenv import load_dotenv
from facts_eng import facts

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


content_var = facts("how big is the universe")
formatted = content_var.split('\n\n', 1)[1]


message = client.messages \
    .create(
        body="I am going to kill you in your sleep",
        from_='+18316182709',
         #replace with your own number 
        to='+13028412936'
    )

print(message.sid)