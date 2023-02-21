from email.message import EmailMessage
import ssl
import smtplib
import datetime as dt
import time

email_sender = input("Enter Your gmail-id : ")
email_password = "xpxfmjhwbjmwxjwl"
email_receiver = input("Enter Receiver's gmail-id : ")

subject = "Happy Birthday!"
body = '''
    Wishing you all the best on your special day



    Thanks and Regards,
    Tejaswini S P
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

with open("Birthday.jpg", 'rb') as f:
    file_data = f.read()
    file_type = '.jpg'
    file_name = f.name

em.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    send_time = dt.datetime(2023,2,9,11,19,0)
    print(send_time.timestamp())
    print(time.time())
    x=time.sleep(send_time.timestamp() - time.time())
    print(x)
    smtp.send_message(em)
    smtp.close()
print("Mail sent successfully")