import smtplib
import requests

# API
response = requests.get(url="https://api.kanye.rest")
data = response.json()
quote = data["quote"]

# Variables
my_email = "email@gmail.com"
password = "password"
message = "Subject: Important message\n\nHello world!"
received_email = ["email@gmail.com", "nextemail@gmail.com"]

# With statement
with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=received_email,
                        msg=quote.encode("utf-8")
                        )
