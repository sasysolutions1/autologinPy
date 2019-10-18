import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




msg = MIMEMultipart('alternative')

me = 'me@gmail.com'
you = 'you@example.com'
msgbody = 'This is the body of the error system, and a test.'
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Error with your amazing software'
msg['From'] = me
msg['To'] = you


mimebody = MIMEText(msgbody, 'plain')
msg.attach(mimebody)
composed = str(msg)
msg.get_payload()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('me@gmail.com', 'password')
s.sendmail('me@gmail.com', 'you@example.com', composed)




s.quit()