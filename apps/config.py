import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("EMAIL_PASSWORD")