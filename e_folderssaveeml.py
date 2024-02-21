import os
import json
import imaplib
import email
from email.header import decode_header
import re

def clean_filename(filename):
    # Substituir caracteres inválidos por "_"
    cleaned_filename = re.sub(r"[^\w\s.]", "_", filename.replace('\r\n', ' '))[:50]
    return cleaned_filename




# Restante do código permanece inalterado...


def download_emails(domain, server, email_address, password, folder_path):
    # Conectar ao servidor IMAP
    imap = imaplib.IMAP4_SSL(server)

    # Fazer login
    imap.login(email_address, password)

    # Selecionar a caixa de entrada (inbox) ou a pasta desejada
    imap.select("inbox")  # Pode ser necessário ajustar para a pasta correta

    # Pesquisar e-mails no domínio específico
    _, messages = imap.search(None, f'(FROM "{domain}")')

    for msg_id in messages[0].split():
        _, msg_data = imap.fetch(msg_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Decodificar o assunto para garantir que seja um nome de arquivo válido
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes) and encoding:
            subject = subject.decode(encoding)

        cleaned_subject = clean_filename(subject)

        # Criar o nome do arquivo com o assunto limpo
        file_name = clean_filename(f"{subject}.eml")

        # Caminho completo para o arquivo
        file_path = os.path.join(folder_path, file_name)

        # Salvar o e-mail como arquivo .eml
        with open(file_path, "wb") as eml_file:
            eml_file.write(raw_email)

        print(f"E-mail salvo: {file_path}")

    # Fechar a conexão com o servidor
    imap.logout()

def filter_emails(emails, whitelist):
    filtered_emails = [email_data for email_data in emails if email_data["dominio"] in whitelist]
    return filtered_emails

def read_whitelist():
    whitelist = []
    if os.path.exists("whitelist.txt"):
        with open("whitelist.txt", "r") as file:
            for line in file:
                whitelist.append(line.strip())
    return whitelist

def read_emails_from_json():
    with open("novo_email_dominio.json", "r") as json_file:
        emails = json.load(json_file)["emails"]
    return emails

os.makedirs("whitelist", exist_ok=True)

whitelist = read_whitelist()
emails = read_emails_from_json()

for domain in whitelist:
    download_emails(domain, "torulog.com.br", "severino@torulog.com.br", "Tr37880693!", "whitelist")

print("E-mails filtrados e salvos conforme a whitelist.")
