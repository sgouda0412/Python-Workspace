import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(from_email, from_password, to_email, subject, body):
    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, from_password)

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


# Zapier passes in `input_data` containing data from the previous steps
from_email = input_data.get("from_email", "default_from_email@example.com")
from_password = input_data.get("from_password", "default_password")
to_email = input_data.get("to_email", "default_to_email@example.com")
subject = input_data.get("subject", "default_subject")
body = input_data.get("body", "default_body")

# Ensure all required fields are present
if not from_email or not from_password or not to_email:
    raise ValueError("Missing required email information")

# Send the email
send_email(from_email, from_password, to_email, subject, body)

# Return a success message
return {"status": "Email sent successfully"}
