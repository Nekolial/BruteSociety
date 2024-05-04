import click
import sys
import time
import requests
import logging
from colorama import init, Fore, Style
from urllib.parse import urlparse

# Inicializar colorama para suportar estilos de texto no terminal
init()

# Configuração de logging
logging.basicConfig(filename='brute_society.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
TIMEOUT = 5

# Função para exibir uma falsa barra de carregamento
def loading_bar():
    print("\nIniciando Brute Society...")
    for _ in range(1):
        print("Bootando ", end="")
        for _ in range(10):
            print("█", end="", flush=True)
            time.sleep(0.2)
        print()

def is_valid_url(url):
    """Verifica se a URL fornecida está em um formato válido."""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

def load_wordlist(wordlist_file):
    """Carrega a wordlist do arquivo fornecido."""
    try:
        with open(wordlist_file, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Arquivo de wordlist não encontrado.")
        logging.error("Arquivo de wordlist não encontrado.")
        sys.exit(1)
    except Exception as e:
        print("Erro ao abrir o arquivo de wordlist:", e)
        logging.error("Erro ao abrir o arquivo de wordlist: %s", e)
        sys.exit(1)

def make_request(url, word, auth=None):
    """Realiza uma solicitação HTTP para a URL com a palavra fornecida."""
    try:
        params = {'word': word}
        response = requests.get(url, params=params, auth=auth, timeout=TIMEOUT)
        code = response.status_code
        if code != 404:
            print("{} -- {}".format(response.url, code))
            logging.info("Solicitação bem-sucedida: %s -- %s", response.url, code)
    except requests.exceptions.RequestException as e:
        print("Erro ao acessar {}: {}".format(url, e))
        logging.error("Erro ao acessar %s: %s", url, e)

@click.command()
@click.option('--open-client', is_flag=True, help='Abrir o cliente')
def main(open_client):
    if open_client:
        print("Abrindo o cliente...")
        # Aqui você pode adicionar o código para abrir o cliente desejado
        # Por exemplo, abrir um navegador web com uma interface gráfica para inserir a URL e a wordlist
    else:
        print(Fore.RED+ Style.BRIGHT + """
  ____             _         ____             _      _         
 | __ ) _ __ _   _| |_ ___  / ___|  ___   ___(_) ___| |_ _   _ 
 |  _ \| '__| | | | __/ _ \ \___ \ / _ \ / __| |/ _ | __| | | |
 | |_) | |  | |_| | ||  __/  ___) | (_) | (__| |  __| |_| |_| |
 |____/|_|   \__,_|\__\___| |____/ \___/ \___|_|\___|\__|\__, |
                                                         |___/                                         
""")
        print(Fore.CYAN + "            BY: Nekolial")
        print(Fore.BLUE + "            GitHub: " + Style.RESET_ALL + "https://github.com/Nekolial\n")

        print(Fore.MAGENTA + "")
        print("A humanidade está presa numa prisão. Vivendo em um mundo que não entende'")
        print("Você é uma fraude. Um holograma. A raiva de outra pessoa.")
        print("01010101010101010101010101010101010101010101010101010101.")
        print("O mundo é uma ilusão. O que fazemos nela é o que importa.")
        print("Tempos empolgantes no mundo agora, tempos empolgantes....")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        loading_bar()

        url = click.prompt('\nPor favor, insira a URL alvo:', type=str)
        if not is_valid_url(url):
            print("URL inválida. Certifique-se de incluir o esquema (http:// ou https://) e o nome do host.")
            logging.error("URL inválida fornecida: %s", url)
            sys.exit(1)
        elif urlparse(url).scheme != 'https':
            print("AVISO: Recomenda-se usar HTTPS para maior segurança.")
            logging.warning("URL não usa HTTPS: %s", url)

        wordlist_file = click.prompt('Por favor, insira o nome do arquivo de wordlist:', type=str)
        wordlist = load_wordlist(wordlist_file)

        loading_bar()

        auth = None
        if click.confirm('Esta URL requer autenticação de usuário?'):
            username = click.prompt('Nome de usuário:', type=str)
            password = click.prompt('Senha:', type=str, hide_input=True)
            auth = (username, password)

        for word in wordlist:
            make_request(url, word, auth)

if __name__ == "__main__":
    main()
