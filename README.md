# 📧 Python Email Sender

A **framework-free Python application** for sending **HTML emails via SMTP**.  
Built with a clean structure, secure configuration, and reusable components.


## 🚀 Features

- Send emails using SMTP
- HTML email support (Jinja2 templates)
- Secure credentials via `.env`
- TLS encryption
- Framework-free architecture


## 🛠 Tech Stack

- Python 3.10+
- smtplib, email, ssl
- python-dotenv
- jinja2


## ⚙️ Setup

```bash
pip install -r requirements.txt
```

## Create a .env file:

```env
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=APP_PASSWORD
```

- Gmail requires an App Password.


## ▶️ Run

```shell
python main.py
```

