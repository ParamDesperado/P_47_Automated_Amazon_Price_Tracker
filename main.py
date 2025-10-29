import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Amazon Product URL (IN)
PRODUCT_URL = "https://www.amazon.in/LEGO-Harry-Potter-Hogwarts-Castle/dp/B07BLDTWVW/"

# Headers help avoid Amazon blocking scraping requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

# Request HTML
response = requests.get(PRODUCT_URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")

# ✅ Extract Product Title
title_elem = soup.select_one("#productTitle")
if not title_elem:
    raise ValueError("Product title not found")

product_name = title_elem.get_text(strip=True)
print(f"Product Name: {product_name}")

# ✅ Extract Price (INR)
price_elem = soup.select_one(".a-price .a-offscreen")
if not price_elem:
    raise ValueError("Price element not found")

price_text = price_elem.get_text(strip=True)
price = float(price_text.replace("₹", "").replace(",", ""))
print(f"Price: ₹{price}")

# ✅ Trigger Alert if below threshold
TARGET_PRICE = 35000

if price < TARGET_PRICE:
    subject = f"Price Alert: {product_name}"
    body = (
        f"{product_name} just dropped to ₹{price}!\n"
        f"Buy here: {PRODUCT_URL}"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:{subject}\n\n{body}"
        )

    print("✅ Email Sent!")
else:
    print(f"No alert sent — price (₹{price}) is above ₹{TARGET_PRICE}")
