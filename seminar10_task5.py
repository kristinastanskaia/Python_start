"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

args = ['ping', 'yandex.ru']
yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
print(yandex_ping.stdout)
for line in yandex_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

args_youtube = ['ping', 'youtube.com']
youtube_ping = subprocess.Popen(args_youtube, stdout=subprocess.PIPE)
print(youtube_ping.stdout)
for line in youtube_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))
