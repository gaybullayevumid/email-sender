import smtplib
import ssl
import os
import re
import logging
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Logging sozlamalari
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EmailSenderError(Exception):
    """Email yuborishda xatolik yuz berdi"""
    pass


class EmailSender:
    def __init__(self, smtp_server, smtp_port, email, password):
        if not all([smtp_server, smtp_port, email, password]):
            raise ValueError("Barcha parametrlar to'ldirilishi kerak!")
        
        if not self._validate_email(email):
            raise ValueError(f"Noto'g'ri email format: {email}")
        
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        logger.info(f"EmailSender yaratildi: {email}")
    
    @staticmethod
    def _validate_email(email):
        """Email formatini tekshirish"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def render_template(self, template_name, context):
        """HTML shablonni render qilish"""
        try:
            # Loyihaning ildiz papkasidan templates papkasini topish
            base_dir = Path(__file__).resolve().parent.parent
            templates_dir = base_dir / "templates"
            
            if not templates_dir.exists():
                raise FileNotFoundError(f"Templates papkasi topilmadi: {templates_dir}")
            
            env = Environment(loader=FileSystemLoader(str(templates_dir)))
            template = env.get_template(template_name)
            logger.info(f"Shablon yuklandi: {template_name}")
            return template.render(context)
        except Exception as e:
            logger.error(f"Shablon render qilishda xatolik: {e}")
            raise EmailSenderError(f"Shablon render qilishda xatolik: {e}")
    
    def send_email(self, to, subject, template_name=None, context=None, body=None):
        """Email yuborish"""
        try:
            # Email formatini tekshirish
            if not self._validate_email(to):
                raise ValueError(f"Noto'g'ri qabul qiluvchi email format: {to}")
            
            # HTML content yaratish
            if template_name and context:
                html_content = self.render_template(template_name, context)
            elif body:
                html_content = body
            else:
                raise ValueError("Template yoki body parametri talab qilinadi!")

            # Email xabarini yaratish
            msg = EmailMessage()
            msg["From"] = self.email
            msg["To"] = to
            msg["Subject"] = subject
            msg.set_content("Bu xabar HTML formatda. Agar ko'rinmasa, email mijozingizni yangilang.")
            msg.add_alternative(html_content, subtype="html")

            # SSL konteksti
            context_ssl = ssl.create_default_context()

            logger.info(f"Email yuborilmoqda: {to}")
            
            # SMTP orqali email yuborish
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.starttls(context=context_ssl)
                server.login(self.email, self.password)
                server.send_message(msg)

            logger.info(f"Email muvaffaqiyatli yuborildi: {to}")
            return True
            
        except smtplib.SMTPAuthenticationError:
            logger.error("SMTP autentifikatsiya xatosi! Email yoki parolni tekshiring.")
            raise EmailSenderError("Email yoki parol noto'g'ri!")
        except smtplib.SMTPException as e:
            logger.error(f"SMTP xatosi: {e}")
            raise EmailSenderError(f"Email yuborishda xatolik: {e}")
        except Exception as e:
            logger.error(f"Kutilmagan xatolik: {e}")
            raise EmailSenderError(f"Email yuborishda kutilmagan xatolik: {e}")