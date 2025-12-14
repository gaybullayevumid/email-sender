import smtplib
import ssl
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader


class EmailSender:
    def __init__(self, smtp_server, smtp_port, email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def render_template(self, template_name, context):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template(template_name)
        return template.render(context)
    
    def send_email(self, to, subject, template_name, context):
        html_content = self.render_template(template_name, context)

        msg = EmailMessage()
        msg["From"] = self.email
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content("Email HTML formatda yuborildi.")
        msg.add_alternative(html_content, subtype="html")

        context_ssl = ssl.create_default_context()


        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls(context=context_ssl)
            server.login(self.email, self.password)
            server.send_message(msg)


        print("Email muvaffaqiyatli yuborildi.")