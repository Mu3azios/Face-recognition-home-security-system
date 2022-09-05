import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import Detector
email_user = 'muaz.AIcamera@gmail.com'
email_password = 'ucsi.fyp.AI'
email_send = 'mu3az.92@gmail.com'

subject = 'Alert'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, someone is trying to access your property'
msg.attach(MIMEText(body,'plain'))
path = "./data/"
filename='warning.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'ucsi.fyp.AI')

server.sendmail(email_user,email_send,text)
server.quit()
