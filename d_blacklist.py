# Código para criar uma blacklist do restante dos emails e salvar em formato .eml

import os
import json

def filter_emails(emails, whitelist):
    filtered_emails = []
    for email_data in emails:
        domain = email_data["dominio"]
        if any(domain.endswith(whitelisted_domain) for whitelisted_domain in whitelist):
            filtered_emails.append(email_data)
    return filtered_emails

def read_whitelist():
    whitelist = []
    with open("whitelist.txt", "r") as file:
        for line in file:
            whitelist.append(line.strip())
    return whitelist

def read_emails_from_json():
    with open("novo_email_dominio.json", "r") as json_file:
        emails = json.load(json_file)["emails"]
    return emails

def read_blacklist():
    blacklist = []
    with open("blacklist.txt", "r") as file:
        for line in file:
            blacklist.append(line.strip())
    return blacklist

os.makedirs("blacklist", exist_ok=True)  # Criar a pasta "blacklist"

whitelist = read_whitelist()
emails = read_emails_from_json()
filtered_emails = filter_emails(emails, whitelist)

# Ler a blacklist para evitar duplicações
existing_blacklist = read_blacklist()

# Adicionar novos e-mails à blacklist (se não estiverem na whitelist)
new_blacklist_emails = [email_data['email'] for email_data in emails if email_data['email'] not in existing_blacklist]
with open("blacklist.txt", "a") as blacklist_file:
    for email in new_blacklist_emails:
        blacklist_file.write(email + "\n")

# Salvar os e-mails da blacklist em formato .eml
for idx, email_data in enumerate(emails):
    if email_data['email'] in new_blacklist_emails:
        eml_content = f"From: {email_data['email']}\nSubject: Sample Subject\n\nSample Body"
        eml_filename = f"blacklist/email_{idx+1}.eml"
        with open(eml_filename, "w") as eml_file:
            eml_file.write(eml_content)

print("E-mails adicionados à blacklist e salvos em formato .eml.")
print("Blacklist criada com sucesso.")