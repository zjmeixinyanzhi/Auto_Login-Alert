#!/usr/bin/python
# -*- coding: utf-8 -*-

from twilio.rest import Client

def send_msg(msg_body):
    # Your Account SID from twilio.com/console
    account_sid = "XXXXXXXXXXXXXXXXXX"
    # Your Auth Token from twilio.com/console
    auth_token  = "XXXXXXXXXXXXXXXXXXXXXXX"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to="+86155********",
    from_="+14433962255",
    body=" "+msg_body)
    if (message.sid):
        print 'Success'
    else:
        print 'Error'

if __name__ == '__main__':
    send_msg('Test')