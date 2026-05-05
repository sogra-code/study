import shutil
import time
import os
import datetime

SOURCE_DIR = '/opt/database'
BACKUP_DIR = '/opt/backup2'

def backup_folder():
    # Получаем текущую дату для имени папки с бэкапом
    now = datetime.datetime.now()
    backup_name = f"backup_{now.strftime('%Y-%m-%d')}"
    dest_path = os.path.join(BACKUP_DIR, backup_name)

    # Копируем папку
    shutil.copytree(SOURCE_DIR, dest_path)
    print(f'Бэкап создан: {dest_path}')

while True:
    now = datetime.datetime.now()
    # Проверяем, не пора ли делать бэкап (21:00)
    if now.hour == 21 and now.minute == 0 and now.second == 0:
        backup_folder()
        # Ждём до следующего дня, чтобы не делать несколько копий
        time.sleep(86400)  # 24 часа
    else:
        # Проверяем каждую секунду
        time.sleep(1)