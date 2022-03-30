import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Using a While loop to make sure that Our code runs all the time (once a day)

while True:
    re = requests.get('http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
    res = re.content

    soup = BeautifulSoup(res, 'html.parser')
    price = float(soup.find('p', class_='price_color').text[1:])

# Checking if the price is less than 40
# Use your email and the password (you can generate a password for the app from your Yahoo account)

    if price < 40:
        smt = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        smt.ehlo()
        smt.starttls()
        # Use your credentials
        smt.login('YourEmail@yahoo.com', 'YourPassword')
        # First email is the sender's email, the second is the receiver's email
        smt.sendmail('Sender@yahoo.com',
                     'Receiver@yahoo.com',
                     f"Subject: Headphones Price Notifier\n\nHi, price has dropped to {price}. Buy it!")
        smt.quit()
    time.sleep(24*60*60)
