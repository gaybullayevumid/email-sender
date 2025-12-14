from apps.config import Config
from apps.sender import EmailSender


def main():
    sender = EmailSender(
        smtp_server=Config.SMTP_SERVER,
        smtp_port=Config.SMTP_PORT,
        email=Config.EMAIL,
        password=Config.PASSWORD
    )

    sender.send_email(
        to="gaybullayevblog@gmail.com",
        subject="Python Email Sender app",
        template_name="email.html",
        context={
            "name": "Umid",
            "message": "Python Email Sender app"
        }
    )

if __name__ == "__main__":
    main()