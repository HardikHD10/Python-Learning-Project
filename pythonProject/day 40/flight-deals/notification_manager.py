import requests
from twilio.rest import Client
import smtplib
account_sid = 'AC55f4b44f413ce614e738bb331bcad369'
auth_token = '9bfb9458851430bed044704341ba553b'

class NotificationManager:
    def send_message_sms(self,message):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message,
            from_='+17744694204',
            to='+919829657691',
        )

        print(message.status)

    def send_email(self,user_email,message):
        my_email = "schoolink06@gmail.com"
        my_password = "dbmkzougjjpnfvmy"

        # sender's email provider
        # smtp.gmail.com
        # smtp.live.com
        # smtp.mail.yahoo.com
        connection = smtplib.SMTP("smtp.gmail.com",587)

        # secure connection
        connection.starttls()

        # connection - login
        connection.login(user=my_email,password=my_password)

        # send email
        connection.sendmail(from_addr=my_email,to_addrs=user_email,msg=f"Subject:Hello\n\n{message}")

        #close connection
        connection.close()