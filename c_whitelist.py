# Código para criar uma whitelist onde você coloca o domínio do email que deseja analisar

# Lista de domínios para análise
whitelist = [
    "torulog.com.br",
    # Adicionar mais domínios conforme necessário
]

# Escrever os domínios em um arquivo de lista branca
with open("whitelist.txt", "w") as file:
    for domain in whitelist:
        file.write(domain + "\n")
print("Whitelist criada com sucesso.")
