# Código para acessar vários servidores e domínios com nomes diferentes

# Importar bibliotecas necessárias
import imaplib

# Dados do servidor
email = "severino@torulog.com.br"
senha = "Tr37880693!"
servidor = "torulog.com.br"

# Conectar ao servidor IMAP
imap = imaplib.IMAP4_SSL(servidor)

# Fazer login
imap.login(email, senha)

# Preparar para adicionar mais emails
# Código para preparar o servidor vai aqui
print(f"Acesso ao servidor {servidor} bem-sucedido.")
# (Incluir código adicional conforme necessário)
