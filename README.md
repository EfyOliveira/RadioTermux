<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="python-logo-generic.svg">
</div>

# RadioTermux

RadioTermux é um script Python simples que permite ouvir estações de rádio diretamente no Termux, um terminal Linux para Android.

## Como usar

1. **Instalação**

    Certifique-se de ter o Python e um player de mídia como o `mpv` ou `mplayer` instalados no seu dispositivo Android com o Termux.

2. **Baixar o script**

    Você pode baixar o script diretamente do repositório
   
```bash
    git clone https://github.com/EfyOliveira/RadioTermux
```

4. **Execução**

    Abra o Termux e navegue até o diretório onde você salvou o arquivo `radiotermux.py`.

```bash
    cd RadioTermux
```

**OBS:**

## Antes do uso execunte o script para baixar tudo que é necessario.

```bash
    bash install.sh
```

   Execute o script com o seguinte comando:

```bash
    python radiotermux.py
```

6. **Escolha uma estação de rádio**

    Ao iniciar o script, você será saudado com uma lista de estações de rádio disponíveis. Basta digitar o número da estação desejada e pressionar Enter para começar a ouvir.

7. **Aproveite**

    Relaxe e aproveite suas estações de rádio favoritas diretamente no seu dispositivo Android através do Termux!

## Personalização

Você pode facilmente personalizar o script adicionando mais estações de rádio à lista `estacoes` no arquivo `radiotermux.py`. Siga as instruções no próprio código para adicionar novas estações.

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).
