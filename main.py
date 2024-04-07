import smtplib

my_email = "email@gmail.com"
password = "password"
message = "Hello world!"
received_email = "email@gmail.com"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=received_email,
                        msg=message.encode("utf-8")
                        )