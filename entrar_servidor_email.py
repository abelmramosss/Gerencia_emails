import imaplib
import json

def carregar_configuracao(arquivo_config):
    with open(arquivo_config) as f:
        return json.load(f)

def conectar_servidor_email(servidor):
    return imaplib.IMAP4_SSL(servidor)

def selecionar_caixa_entrada(conexao):
    conexao.select('inbox')

def main():
    # Carregar configuração
    config = carregar_configuracao('acessos.json')

    # Apenas o primeiro email será usado por enquanto
    primeira_empresa = config['empresas'][0]
    
    # Conectar ao servidor de email
    servidor = conectar_servidor_email(primeira_empresa['servidor'])
    servidor.login(primeira_empresa['email'], primeira_empresa['senha'])
    selecionar_caixa_entrada(servidor)
    # Realize qualquer operação adicional aqui, se necessário
    servidor.close()
    servidor.logout()

    # Mensagem de confirmação
    print("Acesso realizado com sucesso.")

if __name__ == "__main__":
    main()
