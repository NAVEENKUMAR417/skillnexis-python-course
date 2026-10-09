
import csv
import smtplib
import re
from datetime import datetime
from getpass import getpass
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

print("Program started")
sender_email = input("Enter your Gmail address: ").strip()
print("Gmail entered")

app_password = getpass("Enter your Gmail App Password: ").strip()
print("App password entered")

subject = input("Enter your subject: ").strip()
message = input("Enter your message: ").strip()


try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, app_password)

        print("Gmail SMTP connection successful!")

except Exception as error:
    print("Connection failed:", error)

def is_valid_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    if re.match(pattern, email) is None:
        return False

    if email.lower().endswith("@example.com"):
        return False

    return True



if not subject or not message:
    print("Subject and message cannot be empty.")
    raise SystemExit

count = 0
skipped = 0

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for student in reader:
            name = (student.get("name") or "").strip()
            email = (student.get("email") or "").strip()

            # Skip rows with missing information

            if not name or not email or not is_valid_email(email):
                print(f"Skipping invalid row: {name}, {email}")
                skipped += 1

                with open("email_log.csv", "a", newline="", encoding="utf-8") as log_file:
                    writer = csv.writer(log_file)

                    if log_file.tell() == 0:
                        writer.writerow(["Name", "Email", "Timestamp", "Status"])

                    writer.writerow([
                        name,
                        email,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Invalid"
                    ])

                continue

            # Personalize the message
            personalized_message = message.replace("{name}", name)

            email_message = EmailMessage()
            email_message["From"] = sender_email
            email_message["To"] = email
            email_message["Subject"] = subject
            email_message.set_content(personalized_message)

            try:
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(sender_email, app_password)
                    server.send_message(email_message)

                count += 1
                print(f"Email sent to {name} ({email})")

                with open("email_log.csv", "a", newline="", encoding="utf-8") as log_file:
                    writer = csv.writer(log_file)

                    if log_file.tell() == 0:
                        writer.writerow(["Name", "Email", "Timestamp", "Status"])

                    writer.writerow([
                        name,
                        email,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Sent"
                    ])

            except (smtplib.SMTPException, OSError) as error:
                skipped += 1
                print(f"Failed to send to {email}: {error}")

                with open("email_log.csv", "a", newline="", encoding="utf-8") as log_file:
                    writer = csv.writer(log_file)

                    if log_file.tell() == 0:
                        writer.writerow(["Name", "Email", "Timestamp", "Status"])

                    writer.writerow([
                        name,
                        email,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Failed"
                    ])

except FileNotFoundError:
    print("Error: students.csv was not found.")
    raise SystemExit

# Final summary
print("\n===== SUMMARY =====")
print("Emails prepared:", count)
print("Rows skipped:", skipped)
print("Mode: LIVE — email sending enabled.")