import collections
import smtplib

#my_email = "oxygebits@gmail.com"
#my_password = "250601@Phenyo"

#with smtplib.SMTP("smtp.gmail.com") as connection:
   # connection.starttls()
   # connection.login(user=my_email, password=my_password)
  #  connection.sendmail(
#           from = my_email,
      #      to_addre
 #       msg="Subject: Hello\n\nThis is the body of my email."
 #   )
#2015June02___>Yahoo

import datetime as dt

#now = dt.datetime.now()
#year = now.year
#day_of_week = now.weekday()

#print(now.time())
#print(day_of_week)

#date_of_birth = dt.time( hour=15, minute=30)
#print(date_of_birth)

import random

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)
    print(quote)

my_email = "oxygebits@gmail.com"
my_password = "250601@Phenyo"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sekhukhune056@gmail.com",
        msg=quote
    )

collections.Counter("Neoeendbfof")
