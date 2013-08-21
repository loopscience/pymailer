from email.mime.text import MIMEText
import email

def makeUTF8HTMLMessage(body):
    """ Create an HTML message encoded in UTF8 for use in 
        providing to smtplib or another mailer """

    msg = MIMEText(None, 'html', 'utf8') # reset msg to None
    msg.set_payload(body.encode('utf8'))
    charset = email.charset.Charset('utf8')
    charset.header_encoding = email.charset.QP
    charset.body_encoding = email.charset.QP
    del msg['Content-Transfer-Encoding']
    msg.set_charset(charset)
    return msg
