import email
import os

def baixar_emails(servidor, pasta_destino):
    _, data = servidor.search(None, 'ALL')
    ids = data[0].split()

    for email_id in ids:
        _, data = servidor.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        # Gerar um nome único para o arquivo EML
        nome_arquivo = f'email_{email_id.decode()}.eml'
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

        # Salvar o arquivo EML
        with open(caminho_arquivo, 'wb') as f:
            f.write(raw_email)

if __name__ == "__main__":
    # Suponha que você já tenha uma função `conectar_servidor_email()` para acessar o servidor de email
    servidor = conectar_servidor_email()  # Chame sua função para acessar o servidor de email aqui

    # Caminho da pasta para salvar os arquivos EML
    pasta_destino = r'C:\Users\abelm\OneDrive\Documentos\GitHub\Gerencia_emails\eml'

    # Chame a função para baixar e salvar os emails
    baixar_emails(servidor, pasta_destino)
