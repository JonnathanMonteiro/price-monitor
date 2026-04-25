import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
 
def send_alert(product_name, current_price, target_price, url):
    subject = f'Alerta: {product_name} está por R$ {current_price:.2f}!'
    body = f'''
    Produto: {product_name}
    Preço atual: R$ {current_price:.2f}
    Seu alvo:   R$ {target_price:.2f}
    Link: {url}
    '''
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
