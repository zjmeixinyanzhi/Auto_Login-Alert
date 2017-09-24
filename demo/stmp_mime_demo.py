#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib,os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

sender = 'vps@163.com'
password = 'yournerverguess'
receivers = 'zj@163.com,vps@163.com'
attachments = 'D:\excel.xls,D:\logs.zip'
img1 = 'D:\home_count_1.png'
img2 = 'D:\home_count_2.png'

def format_addr(s):
    '''格式化From/To邮件地址,支持中文内容'''
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    #构造附件
def uploadattachments():
    if attachments != -1 and attachments != '':
        for att in attachments.split(','):
            os.path.isfile(att)
            name = os.path.basename(att)
            att = MIMEText(open(att).read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            #将编码方式为utf-8的name，转码为unicode，然后再转成gbk(否则，附件带中文名的话会出现乱码)
            att["Content-Disposition"] = 'attachment; filename=%s' % name.decode('utf-8').encode('gbk')
            msg.attach(att)

def send_mail():
    try:
        s = smtplib.SMTP("smtp.163.com")  # 连接smtp邮件服务器,端口默认是25
        s.login(sender, password)  # 登陆服务器
        uploadattachments()
        for receiver in receivers.split(','):
            s.sendmail(sender, [receiver], msg.as_string())  # 发送邮件
        s.close()
        print '发送邮件成功！'
    except :
        print '发送邮件失败！'


msg = MIMEMultipart('alternative')
msg['Subject'] = u'资源可用提醒' # 利用Header设置utf-8中文编码
msg['From'] = format_addr(u'服务器自动通知 <%s>' % sender)
msg['To'] = receivers

mail_msg = """<html><body>
<p>邮件提醒：已经存在可申请资源,请尽快登录
</p><p><a href="http://www.bj.gov.cn">
http://www.bj.gov.cn</a></p>
<p>资源信息统计：</p>
<p><img src="cid:image1" height="300" width="300"></p>
<p><img src="cid:image2" height="100" width="300" ></p>
<p>本邮件来自服务器自动提醒服务，请勿回复</p>
</body></html>"""

# 如果收件人设备不支持查看HTML邮件，还可以查看纯文本内容
msg.attach(MIMEText(mail_msg, 'plain', 'utf-8'))
msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为邮件正文图片元素
fp = open(img1, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)
fp = open(img2, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image2>')
msg.attach(msgImage)

if __name__ == '__main__':
    send_mail()