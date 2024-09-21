from rich.console import Console
from rich.prompt import Prompt
import requests

console = Console()

def check_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            console.print(f"[green]{url} está online.[/green]")
        else:
            console.print(f"[red]{url} está fora do ar. Status code: {response.status_code}[/red]")
    except requests.exceptions.RequestException as e:
        console.print(f"[yellow]Erro ao acessar {url}: {e}[/yellow]")

def main():
    console.print("[bold cyan]Bem-vindo ao Monitor de Sites Interativo![/bold cyan]")
    while True:
        url = Prompt.ask("Digite a URL do site para verificar (ou 'sair' para encerrar)")
        if url.lower() == 'sair':
            console.print("[bold green]Saindo...[/bold green]")
            break
        check_site(url)

if __name__ == "__main__":
    main()
