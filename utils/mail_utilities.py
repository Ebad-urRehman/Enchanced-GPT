import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def send_email(name, email):
    # Sender's and receiver's email addresses
    sender_email = "ebadinfalltraders@gmail.com"
    receiver_email = "ebadinfalltraders@gmail.com"
    password = st.secrets['general']['MAIL_PASSWORD']  # Use an app password if 2FA is enabled

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "FREE USER"

    body = f"{name}, {email}"
    message.attach(MIMEText(body, "plain"))

    # Connect to the Gmail SMTP server and send the email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

