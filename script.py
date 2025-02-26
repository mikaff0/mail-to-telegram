import os
import email
import requests
from imapclient import IMAPClient

# Umgebungsvariablen auslesen
HOST = os.environ.get('IMAP_SERVER')
USERNAME = os.environ.get('EMAIL_ACCOUNT')
PASSWORD = os.environ.get('EMAIL_PASSWORD')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def sende_telegram_nachricht(betreff, text):
    message = f"<b>{betreff}</b>\n\n{text}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'HTML'}
    requests.post(url, data=payload)

def verarbeite_neue_emails(client):
    messages = client.search(['UNSEEN'])
    for msgid in messages:
        raw_data = client.fetch(msgid, ['RFC822'])[msgid][b'RFC822']
        msg = email.message_from_bytes(raw_data)
        betreff = msg.get('subject', 'Kein Betreff')
        text = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain' and 'attachment' not in str(part.get('Content-Disposition')):
                    charset = part.get_content_charset() or 'utf-8'
                    text += part.get_payload(decode=True).decode(charset, errors='ignore')
        else:
            charset = msg.get_content_charset() or 'utf-8'
            text = msg.get_payload(decode=True).decode(charset, errors='ignore')
        sende_telegram_nachricht(betreff, text)

with IMAPClient(HOST, ssl=True) as client:
    client.login(USERNAME, PASSWORD)
    client.select_folder('INBOX')
    while True:
        client.idle()
        responses = client.idle_check(timeout=30)
        client.idle_done()
        if responses:
            verarbeite_neue_emails(client)
