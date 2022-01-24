import os
from twilio.rest import Client

account_sid = ''  # change with yours
auth_token = ''
my_num = '+16203158812'
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
        body=f"Your verification Code is {user_code}",
        from_=my_num,
        to=f'{phone_number}'
    )
    print(message.status)
    print(message.sid)

