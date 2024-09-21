import requests

def check_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} está online.")
        else:
            print(f"{url} está fora do ar. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

def main():
    while True:
        url = input("Digite a URL do site para verificar (ou 'sair' para encerrar): ")
        if url.lower() == 'sair':
            break
        check_site(url)

if __name__ == "__main__":
    main()
