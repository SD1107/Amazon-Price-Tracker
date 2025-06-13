# 🛒 Amazon Price Tracker with Email Alerts

A Python-based price tracker for Amazon products. This script checks the current price of a product and sends an email notification if the price drops below your specified target.

---

## 🔧 Features

- ✅ Real-time Amazon product price scraping
- 📧 Email alerts using SMTP
- 🔒 Secure environment variable usage for credentials
- 🔍 BeautifulSoup for parsing HTML

---

## 🛠 Technologies Used

- Python 3
- `requests`
- `bs4` (BeautifulSoup)
- `smtplib`
- `dotenv`
- Amazon HTML structure for parsing

---

## ⚙️ How It Works

1. You input the Amazon product URL and your desired target price.
2. The script scrapes the current price using BeautifulSoup.
3. If the current price is **less than your target**, it sends you an email with the product title, price, and link.

---

## 🌐 Environment Variables

Create a `.env` file in your project directory and add:

```env
SMTP_ADDRESS=smtp.yourmailprovider.com
SENDER_EMAIL=your_email@example.com
RECEIVER_EMAIL=recipient_email@example.com
PASSWORD=your_email_password_or_app_password
