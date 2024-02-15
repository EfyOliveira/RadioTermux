import os

# Funções de cor para deixar a saída mais elegante
def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

def cor_verde(texto):
    return f"\033[92m{texto}\033[0m"

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_amarela(texto):
    return f"\033[93m{texto}\033[0m"

# Lista de estações de rádio e seus URLs
estacoes = {
    "1": {"nome": "Radio Rock", "url": "http://89cast.com.br:8000/stream"},
    "2": {"nome": "Jazz Radio", "url": "http://stream.laut.fm/jazzloft"},
    "3": {"nome": "Classic FM", "url": "http://media-ice.musicradio.com/ClassicFMMP3"},
    # Adicione mais estações conforme desejado
}

def escolher_estacao():
    print(cor_azul("Bem-vindo ao RadioTermux! Escolha uma estação de rádio para ouvir:"))
    for chave, estacao in estacoes.items():
        print(cor_verde(f"{chave}: {estacao['nome']}"))
    escolha = input(cor_amarela("Digite o número da estação: "))
    if escolha in estacoes:
        return estacoes[escolha]["url"]
    else:
        print(cor_vermelha("Escolha inválida."))
        return None

def tocar_estacao(url):
    comando = f"mpv --no-video {url}"  # Substitua 'mpv' por 'mplayer' se preferir
    os.system(comando)

if __name__ == "__main__":
    url = escolher_estacao()
    if url:
        tocar_estacao(url)
