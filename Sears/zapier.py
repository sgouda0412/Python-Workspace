import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def fetch_latest_email(email_address, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)
    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    latest_email_id = data[0].split()[-1]

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    body = ""

    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode("utf-8")
    else:
        body = email_message.get_payload(decode=True).decode("utf-8")

    return body


def send_email(from_email, from_password, to_email, subject, body):
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_password)

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


# Replace with your actual Gmail credentials
gmail_email = "your_gmail@gmail.com"
gmail_password = "your_gmail_password"

# Replace with your actual Outlook credentials
outlook_email = "your_outlook@outlook.com"
outlook_password = "your_outlook_password"

# Fetch latest email body from Gmail
email_body = fetch_latest_email(gmail_email, gmail_password)

# Input data for sending email to Outlook
input_data = {
    "from_email": gmail_email,
    "from_password": gmail_password,
    "to_email": outlook_email,
    "subject": "Forwarded email from Gmail to Outlook",
    "body": email_body,
}

# Ensure all required fields are present
from_email = input_data.get("from_email")
from_password = input_data.get("from_password")
to_email = input_data.get("to_email")
subject = input_data.get("subject")
body = input_data.get("body")

if not from_email or not from_password or not to_email:
    raise ValueError("Missing required email information")

# Send email to Outlook
send_email(from_email, from_password, to_email, subject, body)

# Return a success message
print({"status": "Email sent successfully"})
