import random
import smtplib

# my_email = "schoolink06@gmail.com"
# my_password = "dbmkzougjjpnfvmy"
#
# # sender's email provider
# # smtp.gmail.com
# # smtp.live.com
# # smtp.mail.yahoo.com
# connection = smtplib.SMTP("smtp.gmail.com",587)
#
# # secure connection
# connection.starttls()
#
# # connection - login
# connection.login(user=my_email,password=my_password)
#
# # send email
# connection.sendmail(from_addr=my_email,to_addrs="hardikinani1007@gmail.com",msg="Subject:Hello\n\nHi its my first email!")
#
# #close connection
# connection.close()

import datetime as DT

date_time = DT.datetime.now()
year = date_time.year
month = date_time.month
day_of_week = date_time.weekday()
print(day_of_week)
# print(month)
# print(date_time)
# print(year)
# print(type(year))
# print(type(date_time))

date_of_birth = DT.datetime(year=2006,month=12,day=23,hour=4)
# print(date_of_birth)



with open("quotes.txt","r") as file:
    content = file.readlines()


if day_of_week == 1 :
    message = random.choice(content)
    my_email = "schoolink06@gmail.com"
    my_password = "dbmkzougjjpnfvmy"

    connection = smtplib.SMTP("smtp.gmail.com",587)


    connection.starttls()


    connection.login(user=my_email,password=my_password)


    connection.sendmail(from_addr=my_email,to_addrs="vaidik23122006@gmail.com",msg=f"Subject:Hello\n\n{message}")

    connection.close()