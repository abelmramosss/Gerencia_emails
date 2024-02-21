import subprocess

# Executar cada arquivo Python em sequência
scripts = [
    "a_server_access.py",
    #"b_create.json",
    "c_whitelist.py",
    "d_blacklist.py",
    "e_folderssaveeml.py"
]

for script in scripts:
    subprocess.run(["python", script])
print("Execução concluída.")
