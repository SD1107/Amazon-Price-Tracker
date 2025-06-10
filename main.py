from bs4 import BeautifulSoup
import smtplib
import requests
import os
from dotenv import load_dotenv


load_dotenv()


URL=input("Input the Url of the product")
response=requests.get(URL)
data=response.text
# print(response)

soup=BeautifulSoup(data,"html.parser")
price=soup.find(name="span",class_="a-offscreen").getText()
# print(price.split("$")[1])
price_now=float(price.split("$")[1])

target=float(input("Input your target price "))
if(price_now<target):
    title=soup.find(name="span",id="productTitle").getText()
    message=f"{title} is on sale for {price}!"
    # print(title.strip())
    connection=smtplib.SMTP(os.environ["SMTP_ADDRESS"],port=587)
    connection.starttls()
    connection.login(user=os.environ["SENDER_EMAIL"],password=os.environ["PASSWORD"])
    connection.sendmail(from_addr=os.environ["SENDER_EMAIL"],
                        to_addrs=os.environ["RECEIVER_EMAIL"],
                        msg=f"Subject:Amazon price alert!!\n\n{message}\n{URL}".encode("utf-8")
                        )
    connection.close()