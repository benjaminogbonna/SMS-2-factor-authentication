import os
from twilio.rest import Client

account_sid = 'AC7d9582455b737bb1259b5639885ddce7'
# messaging_sid = 'MG480035d91e2677025d7bc9e569922819'
auth_token = '20c59b4fd2306fea7d75e62e328cf2ee'
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

