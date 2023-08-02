import random
import datetime as DT
import pandas
import smtplib

data = pandas.read_csv("birthdays.csv")
dict = data.to_dict(orient="records")

current_datetime = DT.datetime.now()
current_date = current_datetime.day
current_month = current_datetime.month

for y in range(len(dict)):
    if dict[y]["day"] == current_date and dict[y]["month"] == current_month :
        letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]
        random_letter = random.choice(letters)
        with open(f"letter_templates/{random_letter}","r") as file:
            text = file.read()
            contents = dict[y]["name"]
            message = text.replace("[NAME]",contents)
            print(message)

            my_email = "schoolink06@gmail.com"
            my_password = "dbmkzougjjpnfvmy"

            connection = smtplib.SMTP("smtp.gmail.com", 587)

            connection.starttls()

            connection.login(user=my_email, password=my_password)

            connection.sendmail(from_addr=my_email, to_addrs=dict[y]["email"],
                                msg=f"Subject:Happy Birthday!!!\n\n{message}")

            connection.close()





