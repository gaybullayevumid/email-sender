import logging
from apps.config import Config
from apps.sender import EmailSender, EmailSenderError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        # Konfiguratsiyani tekshirish
        Config.validate()
        
        # Email yuboruvchini yaratish
        sender = EmailSender(
            smtp_server=Config.SMTP_SERVER,
            smtp_port=Config.SMTP_PORT,
            email=Config.EMAIL,
            password=Config.PASSWORD
        )

        # Email ma'lumotlari
        recipient_email = input("Qabul qiluvchi email manzilini kiriting: ").strip()
        recipient_name = input("Qabul qiluvchi ismini kiriting: ").strip()
        message = input("Xabar matnini kiriting: ").strip()
        
        # Email yuborish
        sender.send_email(
            to=recipient_email,
            subject="Python Email Sender app",
            template_name="email.html",
            context={
                "name": recipient_name or "Foydalanuvchi",
                "message": message or "Salom!"
            }
        )
        
        print("\n✓ Email muvaffaqiyatli yuborildi!")
        
    except EmailSenderError as e:
        logger.error(f"Email yuborishda xatolik: {e}")
        print(f"\n✗ Xatolik: {e}")
    except ValueError as e:
        logger.error(f"Konfiguratsiya xatosi: {e}")
        print(f"\n✗ Konfiguratsiya xatosi: {e}")
    except KeyboardInterrupt:
        print("\n\nDastur to'xtatildi.")
    except Exception as e:
        logger.error(f"Kutilmagan xatolik: {e}", exc_info=True)
        print(f"\n✗ Kutilmagan xatolik: {e}")


if __name__ == "__main__":
    main()