from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


url = input("Enter Url of Product : ")
user_price = int(input("Enter your convinience price in INR: "))
user_email = input("Enter your email address: ")
header={
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url=url,headers=header)
data = response.text

soap = BeautifulSoup(data, "lxml")
price_scrap = soap.find(name="span",class_="a-price-whole")
price = price_scrap.getText().split(".")[0].split(",")
net_price = int(f"{price[0]}{price[1]}")

if net_price < user_price:
    Message = "You can purchase the product! Product is in your price range!"
else:
    Message = "No go! Product is too costly."


my_email = "schoolink06@gmail.com"
my_password = "dbmkzougjjpnfvmy"

# sender's email provider
# smtp.gmail.com
# smtp.live.com
# smtp.mail.yahoo.com
connection = smtplib.SMTP("smtp.gmail.com",587)

# secure connection
connection.starttls()

# connection - login
connection.login(user=my_email,password=my_password)

# send email
connection.sendmail(from_addr=my_email,to_addrs=user_email,msg=f"Subject:Amazon Price Checker\n\n{Message}")

#close connection
connection.close()






