import os.path
import random
import time
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_email(to, subject, body):
    """
    Sends an email using the Gmail API.

    :param to: Email address of the recipient
    :param subject: Subject of the email message
    :param body: Body of the email message
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    credential_json_path = os.path.abspath('credentials.json')
    token_path = os.path.abspath('token.json')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential_json_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)

        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId='me', body=create_message).execute())

        print(F'Email enviado a {to} con éxito. Mensaje ID: {send_message["id"]}')

    except HttpError as error:
        print(F'An error occurred: {error}')

def main():
    for i in range(1, 11):
        # generar asunto al azar
        subject_options = ['correo a tratar', 'otro asunto']
        subject = random.choice(subject_options)

        # generar cuerpo del correo al azar
        random_number = random.randint(1, 100)
        random_date = datetime.now() - timedelta(days=random.randint(1, 365))
        body = f'id: {random_number}\nfecha: {random_date}'

        # enviar correo
        send_email('jmonasterio@cibernos.com', subject, body)
        print(f'Correo {i} enviado')
        
        # esperar 5 segundos antes de enviar el siguiente correo
        time.sleep(2)

if __name__ == '__main__':
    main()
