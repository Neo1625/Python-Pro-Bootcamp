##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import datetime as dt
import re
import smtplib

import pandas
import random

now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)
#print(today)
# HINT 2: Use pandas to read the birthdays.csv
file = pandas.read_csv('birthdays.csv')
bf_file = pandas.DataFrame(file)
#print(bf_file)
temp = bf_file.to_dict(orient='records')
print(temp)
#print(temp[0]['name'])


# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthdays_dict = {(row.month,row.day): f"{row.name}, {row.email}, {row.year}, {row.month}, {row.day}" for (index, row) in bf_file.iterrows()}
#birthdays_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in file.iterrows()}
#print(birthdays_dict)
#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
same_day = ()
for key, value in birthdays_dict.items():
   if key == today:
       same_day = key
       break
print(same_day)

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
def get_name(today):
    for row in temp:
        if today[0] == row['month'] and today[1] == row['day']:
            return row['name']

def get_email(today):
    for row in temp:
        if today[0] == row['month'] and today[1] == row['day']:
            return row['email']


#print(f"name: {get_name(same_day)}")
rand_int = str(random.randint(1, 3))
with open(f'letter_templates/letter_{rand_int}.txt') as bf_letter:
    new_letter = bf_letter.read().replace("[NAME]", get_name(today))
    print(new_letter)

print(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

my_email = "oxygebits@gmail.com"
my_password = "250601@Phenyo"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=get_email(today),
        msg=new_letter
    )


