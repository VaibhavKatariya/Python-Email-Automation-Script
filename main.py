import pandas as pd
import requests
import json

# Mailgun Configuration (replace with your actual credentials)
MAILGUN_DOMAIN = 'your-domain.com'
MAILGUN_API_KEY = 'your-mailgun-api-key'
SENDER_EMAIL = f'Your Team <admin@{MAILGUN_DOMAIN}>'

# Load recipients
df = pd.read_excel("recipients.xlsx")
email_list = df.get("Email").dropna().tolist()

# Email subject
subject = "👋 Welcome to Our Community!"

# Load HTML template
with open("template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# Track sent and failed emails
sent_emails = []
failed_emails = []

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

batch_size = 1000
for batch in chunk_list(email_list, batch_size):
    try:
        recipient_variables = {}
        batch_emails = []

        for email in batch:
            username = email.split("@")[0]
            recipient_variables[email] = {"name": username}
            batch_emails.append(email)

        html_body = html_template.replace("{{name}}", "%recipient.name%")

        response = requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": SENDER_EMAIL,
                "to": batch_emails,
                "subject": subject,
                "html": html_body,
                "h:Reply-To": "reply-to@domain.com",
                "recipient-variables": json.dumps(recipient_variables)
            }
        )

        if response.status_code == 200:
            print(f"✅ Batch sent to {len(batch_emails)} recipients")
            sent_emails.extend(batch_emails)
        else:
            print(f"❌ Batch failed: {response.text}")
            failed_emails.extend([{'Email': e, 'Error': response.text} for e in batch_emails])

    except Exception as e:
        print(f"❌ Error in batch: {e}")
        failed_emails.extend([{'Email': e, 'Error': str(e)} for e in batch])

if sent_emails:
    pd.DataFrame({'Email': sent_emails}).to_excel("sent_emails.xlsx", index=False)
    print("📄 Sent emails saved to 'sent_emails.xlsx'")

if failed_emails:
    pd.DataFrame(failed_emails).to_excel("failed_emails.xlsx", index=False)
    print("⚠️ Failed emails saved to 'failed_emails.xlsx'")
else:
    print("🎉 All emails sent successfully!")
