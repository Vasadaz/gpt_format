#!/usr/bin/python3
"""
Скрипт для автоматизации форматирования дисков в GPT
1) Сделать автоматизация форматирования
2) Добавить звуковое соправождение с помощью speaker, для слепого форматирования
"""

#import subprocess
import pexpect

"""
try:
    # Передаём в процесс run команду "fdisk -l" ввиде списка ["fdisk", "-l"]
    # capture_output=True При Истине - ответ команды не будет выведен в консоль,
    #   но сохраниться в объекте subprocess.CompletedProcess
    # text=True При Истине - текст stdout сохраняет строко вид, иначе байтовая последовательность.
    # check=True При Истине - поднимается ошибка при её возникновении.
    sudo_pass = subprocess.Popen(["echo", '"1234"'], stdout=subprocess.PIPE)
    cmd_sudo_s = subprocess.Popen(["sudo", "-s"], stdin=sudo_pass)
    cmd_fdisk_l = subprocess.run(["fdisk", "-l"], capture_output=True, text=True, check=True)



except subprocess.CalledProcessError as e:
    # Поднимаем ошибку с её описанием взятого из объекта subprocess.CalledProcessError
    print(f"Ошибка команды {e.cmd}!\n{e.stderr}")

# road_gpt команда "fdisk -l" в файле при отсутствии сервера
file_1 = open("road_gpt")
cmd_fdisk.stdout = file_1.read()
file_1.close()
"""

# Ищем последний подключенный диск. a и b диски не трогать - это raid1.
# cmd_fdisk_list = [el[:-1] for el in cmd_fdisk_l.stdout.split() if "/dev/sd" in el and
#                  not "/dev/sda" in el and not "/dev/sdb" in el][0]

#print(f"Найден диск {cmd_fdisk_list}")

