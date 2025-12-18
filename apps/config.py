import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

class Config:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("EMAIL_PASSWORD")
    
    @classmethod
    def validate(cls):
        """Konfiguratsiya sozlamalarini tekshirish"""
        if not cls.EMAIL:
            raise ValueError(
                "EMAIL o'zgaruvchisi topilmadi! .env faylini tekshiring."
            )
        if not cls.PASSWORD:
            raise ValueError(
                "EMAIL_PASSWORD o'zgaruvchisi topilmadi! .env faylini tekshiring."
            )
        logger.info("Konfiguratsiya tekshirildi va to'g'ri")
        return True