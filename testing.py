# Importing required libraries
from email.message import EmailMessage
import ssl
import smtplib
import schedule
import time

# Sender's email address and password
email_sender = "tejaswinisp2023@gmail.com"
email_password = "xpxfmjhwbjmwxjwl"

# Receiver's email address input and name
name=input("Enter the name of the person ")
email_receiver = input("Enter Receiver's gmail-id : ")


# Email subject and body text
subject = "Happy Birthday!"
body =name +  '''
    Wishing you all the best on your special day



    Thanks and Regards,
    Tejaswini S P
'''

# Creating an email message object
em = EmailMessage()

# Setting the email header fields
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# Adding an image attachment to the email
with open('birthday_image.jpg', 'rb') as f:
    file_data = f.read()
    file_type = '.jpg'
    file_name = f.name
em.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# Function to send the email
def job():
    # Creating a default SSL context
    context = ssl.create_default_context()
    # Connecting to the Gmail SMTP server using SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        # Login using the sender's email address and password
        smtp.login(email_sender, email_password)
        # Sending the email
        smtp.send_message(em)
        smtp.close()
        print("Mail sent successfully")

# Scheduling the email to be sent every hour
schedule.every(1).hour.do(job)

# Running the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)