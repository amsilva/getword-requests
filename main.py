import requests

# URL da sua API

#url = 'http://localhost:5000/hangman-api/getword'  # Altere se necessário
#url = 'http://localhost:5000/hangman-api/getdata'  # Altere se necessário
#url = 'http://localhost:5000/hangman-api/getlist'  # Altere se necessário
url = 'http://localhost:5000/hangman-api/getlist/2'  # Altere se necessário
#url = "https://faccamp.pythonanywhere.com/hangman-api/getword"

def get_message():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta for um erro HTTP
        data = response.json()  # Converte a resposta para JSON
    
        print("Mensagem recebida, TIPO:", type(data))
        print("Mensagem recebida, DATA:", data)

        if type(data) == list :
            for item in data :
                print(f"{item['palavra']},{item['categoria']},{item['complexidade']}")
        else :
            print("Mensagem recebida, PALAVRA:", data['palavra'])
            ##print("Mensagem recebida, CATEGORIA:", data['categoria'])
            ##print("Mensagem recebida, COMPLEXIDADE:", data['complexidade'])

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)

if __name__ == '__main__':
    get_message()