#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smtplib import SMTP

SMTPSVR = 'smtp.163.com'
sender = 'HuaTengMa@163.com'
password = 'YourNerverGuess'
receiver = 'JackMa@163.com'

origHdrs = ['From:' + sender,
            'TO:'+ receiver,
            'Subject:Test msg from python client']
origBody = ['Test', 'Please do not replay', 'THK!']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),
                           '\r\n'.join(origBody)])

def send_mail():
    try:
        handle = SMTP(SMTPSVR)
        handle.login(sender, password)
        handle.sendmail(sender, receiver, origMsg)
        print "邮件发送成功！"
        handle.close()
    except:
        print '邮件发送失败！'

if __name__ == "__main__":
    send_mail()