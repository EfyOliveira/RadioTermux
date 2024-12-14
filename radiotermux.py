import os
import time
import itertools

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
    "1": {"nome": "Radio Antena 1", "url": "https://antenaone.crossradio.com.br/stream/1"},
    "2": {"nome": "89 FM Rádio Rock", "url": "https://www.radios.com.br/play/playlist/31289/listen-radio.m3u"},
    "3": {"nome": "Fita Cassete", "url": "https://server01.ouvir.radio.br:8018/stream?1707979108145"},
    "4": {"nome": "Rádio Blues Jazz", "url": "https://stream-152.zeno.fm/d6dg4e0dytzuv?zs=vBNsuK47TA2jAbIyUeI-bw&1707979282390"},
    "5": {"nome": "Apenas Acústico", "url": "http://server02.ouvir.radio.br:8100/stream?1707979467275"},
    "6": {"nome": "Rádio Energia 97.7 FM", "url": "https://streaming.inweb.com.br/energia?1707979611615"},
    "7": {"nome": "Rádio Hits 106.9 FM", "url": "https://wz7.servidoresbrasil.com:9984/stream?1707979808220"},
    "8": {"nome": "Rádio Jovem Pan 89.5 FM", "url": "https://top80.com.br:9000/stream"},
    "9": {"nome": "Rádio Hot 107 FM", "url": "https://9772.brasilstream.com.br/stream?1707980195817"},
}

def escolher_estacao():
    print(cor_azul("Bem-vindo ao RadioTermux! Escolha uma estação de rádio para ouvir:"))
    for chave, estacao in estacoes.items():
        print(cor_verde(f"{chave}: {estacao['nome']}"))
    escolha = input(cor_amarela("Digite o número da estação: "))
    if escolha in estacoes:
        return estacoes[escolha]["url"], estacoes[escolha]["nome"]
    else:
        print(cor_vermelha("Escolha inválida."))
        return None, None

def tocar_estacao(url, nome):
    print(cor_verde(f"\nReproduzindo agora: {nome} 🎵\n"))
    comando = f"mpv --no-video --really-quiet {url} &"
    os.system(comando)

    # Exibir animação enquanto a música toca
    animacao = itertools.cycle(["█▇▆▅▄▃▂▁", "▁▂▃▄▅▆▇█"])
    try:
        while True:
            print(f"\r🎵 Tocando... {next(animacao)}", end="")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(cor_vermelha("\nInterrompido pelo usuário."))
        os.system("pkill mpv")  # Para o player ao sair

if __name__ == "__main__":
    url, nome = escolher_estacao()
    if url:
        tocar_estacao(url, nome)