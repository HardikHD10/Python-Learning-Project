import requests
from twilio.rest import Client
account_sid = 'AC55f4b44f413ce614e738bb331bcad369'
auth_token = '9bfb9458851430bed044704341ba553b'

class NotificationManager:
    def send_message(self,message):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message,
            from_='+17744694204',
            to='+919829657691',
        )

        print(message.status)