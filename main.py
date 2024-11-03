import requests

# URL da sua API
##url = 'http://localhost:5000/simple-get'  # Altere se necessário
#url = 'http://localhost:5000/complex-get'  # Altere se necessário
url = "https://faccamp.pythonanywhere.com/complex-get"

def get_message():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta for um erro HTTP
        data = response.json()  # Converte a resposta para JSON
        
        print("Mensagem recebida, COMPLETA:", data)
        print("Mensagem recebida, PALAVRA:", data['palavra'])
        print("Mensagem recebida, CATEGORIA:", data['categoria'])
        print("Mensagem recebida, COMPLEXIDADE:", data['complexidade'])

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)

if __name__ == '__main__':
    get_message()