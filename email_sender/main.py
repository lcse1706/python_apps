import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders


# Tworzenie wiadomości e-mail
msg = MIMEMultipart()
msg['From'] = 'lukasterra89@gmail.com'
msg['To'] = 'losiu1706@gmail.com'
msg['Subject'] = 'Temat wiadomości'

# Dodanie treści do wiadomości
tekst = 'Cześć! Oto przykładowa wiadomość e-mail z załącznikiem obrazka.'
msg.attach(MIMEText(tekst, 'plain'))


# Wczytanie obrazka i dodanie jako załącznik
with open('obrazek.jpg', 'rb') as file:
    img = MIMEImage(file.read(), name='obrazek.jpg')
    msg.attach(img)

    
# Konfiguracja serwera SMTP i wysłanie wiadomości
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('lukasterra89@gmail.com', 'Opinie123')
server.send_message(msg)
server.quit()