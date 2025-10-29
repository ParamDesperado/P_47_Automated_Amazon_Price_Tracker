# 🛍️ Amazon Price Tracker (India)

A Python automation script that tracks the price of an **Amazon.in product** and sends an **email alert** when the price drops below your target threshold.  
Perfect for smart shoppers and automated deal hunting! 🤑

---

## 📌 Features

✔ Tracks any Amazon.in product price (in ₹ INR)  
✔ Sends an email alert when the price drops  
✔ Scrapes product name & price automatically  
✔ Protects secrets using `.env`  
✔ Fully customizable target price  

---

## 🧰 Tech Stack

| Component | Purpose |
|----------|---------|
| Python | Core application |
| BeautifulSoup4 | Web scraping |
| Requests | Fetch Amazon HTML |
| smtplib | Email notifications |
| .env | Secure credentials |

---

## 🚀 How It Works

1️⃣ The script scrapes the product title + price  
2️⃣ Cleans the INR price format (₹ + commas removed)  
3️⃣ Compares price with your alert threshold  
4️⃣ Sends an email if the price is lower ✅  

---

## 📸 Example Console Output
```
Product Name: LEGO Harry Potter Hogwarts Castle
Price: ₹29990.0
✅ Email Sent!
```

---

## 📥 Installation

### ✅ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Amazon-Price-Tracker.git
cd Amazon-Price-Tracker
```

### ✅ Install Required Packages

```bash
pip install -r requirements.txt
```

> ⚠️ Ensure you have **Python 3.8+** installed

---

## 🔐 Environment Variables Setup (.env)

Create a `.env` file inside your project folder:

```
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
TO_EMAIL=recipient_email@gmail.com
```

📌 Gmail Users:  
You **must** generate a *16-digit App Password*  
(Requires 2-Step Verification Enabled)

👉 https://myaccount.google.com/apppasswords

---

## 🏁 Run the Script

```bash
python main.py
```

---

## ⚙️ Customization

Modify the target price and target Url accordingly but make note that amazon may make changes to the price scraping attribute.
---
## 👨‍💻 Author

Created by  — Param Sangani 🚀
Feel free to ⭐ star the repo & contribute!
