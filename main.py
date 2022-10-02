from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
my_mail = "shreekantpukale16@gmail.com"
my_password = 'your password'
head = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url="https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C57XLR/ref=sr_1_1?crid=25C8MIJFAEYD8&keywords=macbook+pro&qid=1664704548&qu=eyJxc2MiOiI2LjM5IiwicXNhIjoiNi40OCIsInFzcCI6IjUuOTIifQ%3D%3D&sprefix=macbook+pr%2Caps%2C310&sr=8-1", headers=head)
soup = BeautifulSoup(response.content, 'lxml')
price = float(soup.find('span', {'class': 'a-offscreen'}).get_text().split('$')[1].replace(',', ''))
if price < 1200:
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=my_password, password=my_password)
    connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg="SUBJECT:HURRY UP MACKBOOK ON SALE\n\n")
    connection.close()
