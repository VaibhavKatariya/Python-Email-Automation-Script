
# 🚀 Python Bulk Email Automation Script

This is a Python script that sends personalized HTML emails to a list of recipients using the **Mailgun API**. It supports batch sending (up to 1000 emails at a time), error tracking, and logs both successful and failed deliveries into Excel files.

## ✨ Features

- ✅ Send personalized HTML emails in bulk via Mailgun
- 📄 Read recipient emails from an Excel file
- 🔁 Automatic batching of emails (1000 per batch)
- 💡 Uses `{{name}}` placeholders for dynamic personalization
- 🧾 Logs sent and failed emails to Excel
- 📤 Handles Mailgun's recipient variables for personalization

### Batch Sent Output
```bash
✅ Batch sent to 1000 recipients
📄 Sent emails saved to 'sent_emails.xlsx'
```

### Batch Failed Output
```bash
❌ Batch failed: [Mailgun Error Message]
⚠️ Failed emails saved to 'failed_emails.xlsx'
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VaibhavKatariya/Mailgun-Email-Automation-Script.git
```

### 2. Install Dependencies

Make sure you have the required Python packages installed:

```bash
pip install pandas requests openpyxl
```

### 3. Prepare Excel File

Ensure your Excel file (e.g. `email.xlsx`) has a column named **"Email"** with valid recipient email addresses.

### 4. Add Your HTML Template

Create an `index.html` file in the project root containing your email body. You can use `{{name}}` as a placeholder for recipient names.

### 5. Configure Mailgun

In the script, set the following variables with your Mailgun credentials:

```python
MAILGUN_DOMAIN = 'your-domain.com'
MAILGUN_API_KEY = 'your-mailgun-api-key'
SENDER_EMAIL = f'Your Name <admin@{MAILGUN_DOMAIN}>'
```

> 🛡️ **Keep your API key safe.** Use environment variables in production.

### 6. Run the Script

```bash
python main.py
```

---

## 📂 Output Files

- **sent_emails.xlsx**: Contains a list of all successfully sent emails.
- **failed_emails.xlsx**: Contains failed email addresses and their respective error messages.

---

## 📌 Personalization

Use `{{name}}` in your HTML body (index.html). It will automatically be replaced using the prefix of the email address.

```html
<p>Hello {{name}},</p>
<p>Welcome to our event!</p>
```
---
Made with ❤️ for the BitBox Hackathon (GDG JIIT 128).
