import os
import subprocess
import shutil
import sys
from colorama import init, Fore

# Инициализация colorama для раскрашивания текста
init(autoreset=True)

def print_ascii():
    print(Fore.RED + """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠤⠤⠤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣤⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠉⠓⠦⣤⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⡄⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀
⠀⠀⣠⠞⠁⠀⠀⣀⣠⣏⡀⠀⢠⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⡃⠀⠀⠄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆         Iphone_Parser
⢀⡞⠁⠀⣠⠶⠛⠉⠉⠉⠙⢦⡸⣿⡿⠀⠀⠀⡄⢀⣀⣀⡶⠀⠀⠀⢀⡄⣀⠀⣢⠟⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃        creator: ♡𝔡3𝔯𝔯𝔨1𝔞♡
⡞⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⢳⢀⣠⠀⠀⠀⠉⠉⠀⠀⣀⠀⠀⠀⢀⣠⡴⠞⠁⠀⠀⠈⠓⠦⣄⣀⠀⠀⠀⠀⣀⣤⠞⠁⠀                                     
⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠁⠀⢀⣀⣀⡴⠋⢻⡉⠙⠾⡟⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠉⠉⠀⠀⠀⠀
⠘⣦⡀⠀⠀⠀⠀⠀⠀⣀⣤⠞⢉⣹⣯⣍⣿⠉⠟⠀⠀⣸⠳⣄⡀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠒⠒⠒⠒⠒⠚⠋⠁⠀⡴⠋⢀⡀⢠⡇⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⢀⡾⠋⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠉⠋⠻⣄⠀⠀⠀⠀⠀⣀⣠⣴⠞⠋⠳⠶⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠦⢤⠤⠶⠋⠙⠳⣆⣀⣈⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)


def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды '{command}': {e}")
        exit(1)

def cls():
    run_command("clear")
    print_ascii()

# ----

def count_photos_in_directory(directory):
    photo_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.heic', '.thm', '.mp4', '.mov')  # Расширения для различных файлов
    photo_count = 0
    total_size = 0  # Инициализируем переменную для общего размера

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(photo_extensions):
                photo_count += 1
                total_size += os.path.getsize(os.path.join(root, file))  # Суммируем размеры

    return photo_count, total_size


def search_photos():
    connect_iphone()
    iphone_directory = '~/iphone'  # Путь к директории с фото

    if os.path.exists(os.path.expanduser(iphone_directory)):
        total_photos, total_size = count_photos_in_directory(os.path.expanduser(iphone_directory))
        print(f"На устройстве найдено {total_photos} фотографий.")
        print(f"Общий размер фотографий: {total_size / (1024 * 1024):.2f} МБ.")
    else:
        print("Устройство iPhone не подключено или путь не найден.")

    deactivate_iphone()


def deactivate_iphone():
    run_command("fusermount -u ~/iphone")


def is_mounted(directory):
    result = subprocess.run(f"mount | grep {directory}", shell=True, stdout=subprocess.PIPE)
    return result.returncode == 0


def connect_iphone():
    if is_mounted("~/iphone"):
        run_command("fusermount -u ~/iphone")
    run_command("mkdir -p ~/iphone")
    run_command("ifuse ~/iphone")
    print("iPhone успешно подключен и смонтирован.")


def copy_with_unique_name(src, dst, repeat_dir):
    """Копирование файла с добавлением суффикса, если файл с таким именем уже существует."""
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
    else:
        # Перемещение в папку повторяющихся файлов
        shutil.copy2(src, os.path.join(repeat_dir, os.path.basename(src)))
        print(f"Файл с таким же именем найден. Файл перемещен в папку 'repeat': {os.path.basename(src)}")

def download_photos(file_type):
    connect_iphone()
    iphone_directory = '~/iphone'  # Путь к директории с фото
    download_directory = './downloaded_photos'  # Путь, куда будут скачиваться файлы

    # Создаем все подкаталоги сразу, чтобы избежать ошибок
    subdirs = {
        'photos': os.path.join(download_directory, 'photos'),
        'videos': os.path.join(download_directory, 'videos'),
        'gifs': os.path.join(download_directory, 'gifs'),
        'others': os.path.join(download_directory, 'others'),
        'repeat': os.path.join(download_directory, 'repeat')  # Папка для повторяющихся файлов
    }

    for subdir in subdirs.values():
        os.makedirs(subdir, exist_ok=True)  # Создаем подкаталоги для всех типов файлов

    # Определяем расширения файлов для разных категорий
    extensions = {
        'photos': ('.jpg', '.jpeg', '.png', '.heic'),
        'videos': ('.mp4', '.mov'),
        'gifs': ('.gif',),
    }

    if file_type == 'all':
        allowed_extensions = extensions['photos'] + extensions['videos'] + extensions['gifs']
    elif file_type == 'photos':
        allowed_extensions = extensions['photos']
    elif file_type == 'videos':
        allowed_extensions = extensions['videos']
    elif file_type == 'gifs':
        allowed_extensions = extensions['gifs']
    else:
        allowed_extensions = ()

    # Подсчитываем общее количество файлов для загрузки
    total_photos = sum(
        1 for root, dirs, files in os.walk(os.path.expanduser(iphone_directory))
        for file in files if any(file.lower().endswith(ext) for ext in allowed_extensions)
    )
    
    if total_photos == 0:
        print("Нет файлов для скачивания.")
        deactivate_iphone()
        return

    print(f"Начинаем скачивание {total_photos} файлов...")

    downloaded_photos = 0

    for root, dirs, files in os.walk(os.path.expanduser(iphone_directory)):
        for file in files:
            if file.lower().endswith(extensions['photos']):
                destination = os.path.join(subdirs['photos'], file)
            elif file.lower().endswith(extensions['videos']):
                destination = os.path.join(subdirs['videos'], file)
            elif file.lower().endswith(extensions['gifs']):
                destination = os.path.join(subdirs['gifs'], file)
            else:
                destination = os.path.join(subdirs['others'], file)

            copy_with_unique_name(os.path.join(root, file), destination, subdirs['repeat'])  # Передаем папку для повторов
            downloaded_photos += 1
            progress_bar(downloaded_photos, total_photos)

    print(f"\nСкачивание завершено. Скачано {downloaded_photos} файлов.")
    deactivate_iphone()



def progress_bar(current, total):
    bar_length = 50
    percent = (current / total)
    arrow = '█' * int(round(percent * bar_length)) + '-' * (bar_length - int(round(percent * bar_length)))
    print(f"\r[{arrow}] {current}/{total}", end='')


def soon():
    print("Функция скоро будет добавлена.")


def main():
    print_ascii()
    while True:
        print(Fore.MAGENTA + """
            1) Search (поиск фотографий)
            2) Download (скачать фотографии)
            3) Exit (выход)
              """)

        choice = input("")

        if choice == '1':
            search_photos()
        elif choice == '2':
            cls()
            print(Fore.CYAN + """
                1) Скачать всё (гифки, видео, фото)
                2) Скачать только фото
                3) Скачать только видео
                4) Назад
                  """)
            download_choice = input("")

            if download_choice == '1':
                download_photos('all')
            elif download_choice == '2':
                download_photos('photos')
            elif download_choice == '3':
                download_photos('videos')
            elif download_choice == '4':
                continue
            else:
                print("Неверный выбор, попробуйте снова.")
        elif choice == '3':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == '__main__':
    main()
