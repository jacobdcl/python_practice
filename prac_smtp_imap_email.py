import smtplib as smtp
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.utils
from email import encoders

# attachment
with open('prac_msgbot.py','rb') as f:
    msgbotfile = f
    msgbot = MIMEBase('application','octet-stream') 
    msgbot.set_payload((msgbotfile).read())
    encoders.encode_base64(msgbot)
    msgbot.add_header('Content-Disposition', f'attachment; filename="prac_msgbot.py"')

# email metadata
msg = MIMEMultipart()
msg['From'] = 'jakepytest@outlook.com'
password = 'PASSWORD'
msg['To'] = 'jacobdecorelurker@gmail.com'
msg['Subject'] = 'iMessage/Mail Bot'
msg['CC'] = ''
msg['BCC'] = ''
msg['Reply-To'] = ''
msg['Date'] = email.utils.formatdate(localtime=True)
msg['Message-ID'] = email.utils.make_msgid()
msg.attach(msgbot) #attach the file

# email body
text = "I just sent the file to my personal email and it works. If it doesn't work for you its probably because it got flagged by baruch again. I dont have your personal email."
body_text = f"{text}\n\nJake"
body = MIMEText(body_text,'plain')
msg.attach(body)
message = msg.as_string()

# send the email with smtp
server = smtp.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login(msg['From'],password)
print('Login success!')
server.sendmail(msg['From'],msg['To'],message)
print('Sent!')
server.quit()

