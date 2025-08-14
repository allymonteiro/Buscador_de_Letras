import requests
from colorama import Fore, Style, init

def buscar_letra():
    init(autoreset=True)

    print(Style.BRIGHT + Fore.CYAN + "--- BUSCADOR DE LETRAS DEMÚSICA ---")

    artista = input("Digite o nome do artista: ").strip()
    musica = input("Digite o nome da música: ").strip()

    if not artista or not musica:
        print(Fore.RED + "O nome do artista e da música não podem estar vazios.")
        return
    
    url = f"https://api.lyrics.ovh/v1/{artista}/{musica}"

    print(Fore.YELLOW + f"\nBuscando a letra de '{musica}' de '{artista}'...")

    try:
        response = requests.get(url)

        if  response.status_code == 404:
            print(Fore.RED + "Letra não encontrada. Verifique se os nomes estão corretos.")
            return
        
        response.raise_for_status()

        dados = response.json()

        texto_letra = dados['lyrics']

        print(Style.BRIGHT + Fore.GREEN + f"\n--- {musica.upper()} - {artista.upper()} ---")
        print(Fore.WHITE + texto_letra)
        print(Style.BRIGHT + Fore.GREEN + "--------------------------------------------------")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erro de conexão: {e}")
    except Exception as e:
        print(Fore.RED + f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    buscar_letra()
    input("\nPressione Enter para sair.")