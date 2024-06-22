import ssl
import smtplib
from email.message import EmailMessage

subject = "Email from Python"
body= "This is a text email from python!"
sender_email=("yuvrajjain722@gmail.com")
receiver_email =("yuvrajjain722@gmail.com")
password =input("Enter you Password:")

message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message       .set_content(body)

context=ssl.create_default_context()

print("sending email...")

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)

print("Email sent Successfully!")