import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from exchangelib import DELEGATE, Account, Credentials, Message, HTMLBody


def send_email_gmail(from_email, password, to_email, subject, body):
    """
    Function to send an email from a Gmail account.

    :param from_email: str - Sender's Gmail address.
    :param password: str - Password for the sender's Gmail account.
    :param to_email: str - Recipient's email address.
    :param subject: str - Subject of the email.
    :param body: str - Body content of the email.
    """
    # Create a MIME object to represent the email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))  # Attach the email body in plain text

    # Connect to Gmail's SMTP server and log in
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(from_email, password)

    # Send the email
    server.send_message(msg)
    server.quit()  # Close the connection to the server


def send_email_outlook(username, password, to_email, subject, body):
    """
    Function to send an email from an Outlook account using exchangelib.

    :param username: str - Sender's Outlook email address.
    :param password: str - Password for the sender's Outlook account.
    :param to_email: str - Recipient's email address.
    :param subject: str - Subject of the email.
    :param body: str - Body content of the email.
    """
    # Set up credentials and create an account object
    credentials = Credentials(username, password)
    account = Account(
        primary_smtp_address=username,
        credentials=credentials,
        autodiscover=True,
        access_type=DELEGATE,
    )

    # Create the email message
    email = Message(
        account=account,
        folder=account.sent,
        subject=subject,
        body=HTMLBody(body),  # Email body in HTML format
        to_recipients=[to_email],  # List of recipients
    )
    email.send()  # Send the email


def main():
    """
    Main function to demonstrate sending emails from both Gmail and Outlook.
    """
    # Send email from Gmail
    from_email = "santoshtest237@gmail.com"
    gmail_password = "oeos qyln sbaw dtye"
    to_email_gmail = "santosh.gouda@transformco.com"
    subject_gmail = "Test Email from Gmail"
    body_gmail = "This is a test email sent from Gmail."

    print(f"Sending email from Gmail to {to_email_gmail}...")
    send_email_gmail(
        from_email, gmail_password, to_email_gmail, subject_gmail, body_gmail
    )
    print("Email sent successfully from Gmail.")

    # Send email from Outlook
    outlook_username = "santosh.gouda@transformco.com"
    outlook_password = "Welcome@1234567"
    to_email_outlook = "panchanan.jha@transformco.com"
    subject_outlook = "Test Email from Outlook"
    body_outlook = "This is a test email sent from Outlook."

    print(f"Sending email from Outlook to {to_email_outlook}...")
    send_email_outlook(
        outlook_username,
        outlook_password,
        to_email_outlook,
        subject_outlook,
        body_outlook,
    )
    print("Email sent successfully from Outlook.")


if __name__ == "__main__":
    main()
