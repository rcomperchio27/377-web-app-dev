email_user_name = 'rcomperchio27@hanoverstudents.org'
email_app_password = input('Enter your password: ')

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content('This is a test message')
msg['Subject'] = 'Test message 1'
msg['From'] = email_user_name
msg['To'] = 'rcomperchio27@hanoverstudents.org'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    print('Authenticating...')
    server.login(email_user_name, email_app_password)
    print('Sending...')
    server.send_message(msg)
    server.quit()
    print('Message Sent!')
