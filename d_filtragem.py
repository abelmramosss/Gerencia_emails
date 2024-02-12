import email
import os
from collections import defaultdict

def comparar_emails(email1, email2):
    return email1['subject'] == email2['subject'] \
           and email1['from'] == email2['from'] \
           and email1['date'] == email2['date'] \
           and email1.get_payload() == email2.get_payload()

def identificar_emails_repetidos(emails):
    emails_repetidos = defaultdict(list)

    for idx, email_data in enumerate(emails):
        encontrado = False
        for chave, emails in emails_repetidos.items():
            if comparar_emails(email_data, emails[0]):
                emails.append(email_data)
                encontrado = True
                break
        if not encontrado:
            emails_repetidos[idx] = [email_data]

    return emails_repetidos

def excluir_emails_repetidos(emails_repetidos):
    emails_filtrados = []
    for chave, emails in emails_repetidos.items():
        if len(emails) == 1:
            emails_filtrados.append(emails[0])
    return emails_filtrados

def ler_arquivos_eml_na_pasta(caminho_pasta):
    emails = []
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.eml'):
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            with open(caminho_arquivo, 'rb') as f:
                email_data = email.message_from_binary_file(f)
                emails.append(email_data)
    return emails

caminho_pasta_eml = 'C:/Users/abelm/OneDrive/Documentos/EML_salvos'
emails = ler_arquivos_eml_na_pasta(caminho_pasta_eml)

emails_repetidos = identificar_emails_repetidos(emails)
emails_filtrados = excluir_emails_repetidos(emails_repetidos)

for email_data in emails_filtrados:
    """print('Assunto:', email_data['subject'])
    print('Remetente:', email_data['from'])
    print('Data:', email_data['date'])
    print('Conteúdo:', email_data.get_payload())
    print('-' * 50)"""
