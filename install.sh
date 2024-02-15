apt update && upgrade
pkg install mpv
pkg install mplayer


#!/bin/bash
#Script criado para auxiliar o uso do script deixando tudo certo.


clear
echo -e "\e[1;92m Vamos começar atualizando o \e[1;93mTermux."
echo -e "\e[1;92m O processo será breve."

sleep 4
cd ~
apt update -y
apt upgrade -y
clear

sleep 4
echo -e "\e[1;92m Finalizamos a primeira parte. Vamos continuar!"
echo -e "\e[1;93m Instalando o mpv, mplayer e o youtube-dl..."
echo -e "\e[1;92m Se a instalação parar e lhe for pedido alguma coisa, basta aceitar digitando 'Y' e clicando em enter."

sleep 4
cd ~
pkg inatall mpv -y
pkg install mplayer -y
pkg install youtube-dl -y
clear

echo -e "\e[1;92m É isso! Você instalou e atualizou o necessario para começar o uso."
