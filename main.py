import requests

# URL da sua API
url = 'http://localhost:5000/get'  # Altere se necessário

def get_message():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta for um erro HTTP
        data = response.json()  # Converte a resposta para JSON
        print("Mensagem recebida, data:", data)
        print("Mensagem recebida, data['palavra']:", data['palavra'])

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)

if __name__ == '__main__':
    get_message()