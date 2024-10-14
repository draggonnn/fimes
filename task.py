import smtplib
from email.mime.text import MIMEText

def send_email(to_email, course_name):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'seuemail@gmail.com'
    smtp_pass = 'suasenha'

    msg = MIMEText(f'Obrigado por comprar o curso {course_name}!')
    msg['Subject'] = 'Confirmação de Compra'
    msg['From'] = smtp_user
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, to_email, msg.as_string())
