import smtplib
import pandas
import datetime as dt
from random import choice

MY_EMAIL = "test@test.com"
PASSWORD = "test123"

data = pandas.read_csv("birthdays.csv")
birthday_data = pandas.DataFrame(data)
birthday_person = birthday_data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for person in birthday_person:
    if person["month"] == month and person["day"] == day:
        letter = choice(letters)

        with open(letter, "r") as birthday_letter:
            contents = birthday_letter.read()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )
