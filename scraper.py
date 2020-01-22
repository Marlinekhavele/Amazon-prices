import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Canon-Digital-Camera-18-55mm-75-300mm/dp/B01CQJHJ2E/ref=sr_1_3?keywords=canon+camera&qid=1576519423&sr=8-3"

headers = {
    "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    if converted_price < 1.700:
        send_mail()
    print(converted_price)
    print(title.strip())
 
    if(converted_price > 1.700):
        send_mail()


def send_mail():
    server - smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls
    server.ehlo()
    server.login("khavelemarline@gmail.com", "marline1998")

    subject = "Price went up!"
    body = 'check amazon link https://www.amazon.com/Canon-Digital-Camera-18-55mm-75-300mm/dp/B01CQJHJ2E/ref=sr_1_3?keywords=canon+camera&qid=1576519423&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'khavelemarline@gmail.com',
        'kmarlinek@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT')

    server.quit()

while(True): 
    check_price()
    time.sleep(60*60)

