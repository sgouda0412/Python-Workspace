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


if __name__ == "__main__":
    # Define the email details
    from_email = "santoshtest237@gmail.com"
    from_password = "oeos qyln sbaw dtye"
    to_email = "santosh.gouda@transformco.com"
    subject = "test mail"
    body = "This is a test email from gmail"

    # Send the email
    send_email(from_email, from_password, to_email, subject, body)
