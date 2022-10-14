

$ termux-setup-storage # предоставление доступа к хранилищу
$ pkg show ffmpeg # «оно ли это» #получить мета-информацию о пакете
$ termux-change-repo # Выбрать получение обновлений (для всех репо, их может быть больше одного) с другого хостинга, которое не цензурируется вашим провайдером (на мой взгляд самое стабильное зеркало репозитория в РФ — это зеркало Termux/Github).

$ nano -$ .termux/termux.properties #настроки termux
$ termux-reload-settings #перезапуск


# установленно 03.10.22
$ pkg update && pkg install curl git grep
 # установки:
06.10.22 nmap #сканер сети
08.10.22 nodejs (npm) для запуска  outline-client(shh VPN)
08.10.22 link #хз что
08.10.22 links # браузер
08.10.22 openVPN прог для развнртывания VPN ❕wget https://git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh
# хорошая но большая инструкция openvpn https://habr.com/ru/post/233971/
09.10.22 speedtest-cli тест скорости интернета есть питон опция
10.10.22 vk vr_api # примеры работыс vk
