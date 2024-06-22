import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_mail, from_):
    from_password = "fwqo idve pjyt izmr"  # This should be securely handled

    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to_mail
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_, from_password)
        text = msg.as_string()
        server.sendmail(from_, to_mail, text)
        server.quit()
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {e}"
