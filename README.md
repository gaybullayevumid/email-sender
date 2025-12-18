# 📧 Python Email Sender

A **framework-free Python application** for sending **HTML emails via SMTP**.  
Built with a clean structure, secure configuration, and reusable components.


## 🚀 Features

- ✉️ Send emails using SMTP
- 🎨 HTML email support (Jinja2 templates)
- 🔒 Secure credentials via `.env`
- 🛡️ TLS encryption
- ✅ Email validation
- 📝 Comprehensive logging
- ⚠️ Error handling and custom exceptions
- 🧪 Interactive input mode
- 📂 Dynamic template path resolution


## 🛠 Tech Stack

- Python 3.10+
- smtplib, email, ssl
- python-dotenv
- jinja2
- logging


## ⚙️ Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create a `.env` file:**
```bash
# Copy the example file
cp .env.example .env
```

3. **Configure your credentials in `.env`:**
```env
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 🔐 Gmail App Password Setup

Gmail requires an **App Password** for SMTP:
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Navigate to **App passwords**
4. Generate a new app password
5. Use that password in your `.env` file


## ▶️ Run

```bash
python main.py
```

The application will prompt you for:
- Recipient email address
- Recipient name
- Message content


## 📁 Project Structure

```
email-sender/
├── apps/
│   ├── config.py          # Configuration management
│   └── sender.py          # Email sending logic
├── templates/
│   └── email.html         # Email template
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── .env.example           # Environment variables example
└── README.md             # Documentation
```


## 🔧 Usage Example

```python
from apps.config import Config
from apps.sender import EmailSender

# Initialize sender
sender = EmailSender(
    smtp_server=Config.SMTP_SERVER,
    smtp_port=Config.SMTP_PORT,
    email=Config.EMAIL,
    password=Config.PASSWORD
)

# Send email
sender.send_email(
    to="recipient@example.com",
    subject="Hello",
    template_name="email.html",
    context={"name": "John", "message": "Welcome!"}
)
```


## 🐛 Error Handling

The application includes comprehensive error handling:
- ✅ Email format validation
- ✅ SMTP authentication errors
- ✅ Connection timeouts
- ✅ Template rendering errors
- ✅ Configuration validation


## 📝 Logging

All operations are logged with timestamps and severity levels:
- INFO: Successful operations
- ERROR: Failed operations with details


## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.


## 📄 License

This project is open source and available under the MIT License.

