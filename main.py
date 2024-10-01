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
⠀⠈⠙⠒⠒⠒⠒⠚⠋⠁⠀⡴⠋⢀⡀⢠⡇⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⢀⡾⠋⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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


def download_photos(file_type):
    connect_iphone()
    iphone_directory = '~/iphone'  # Путь к директории с фото
    download_directory = './downloaded_photos'  # Путь, куда будут скачиваться фото

    os.makedirs(download_directory, exist_ok=True)  # Создаем папку для скачивания, если она не существует

    if file_type == 'all':
        subdirs = {
            'photos': os.path.join(download_directory, 'photos'),
            'gifs': os.path.join(download_directory, 'gifs'),
            'videos': os.path.join(download_directory, 'videos'),
            'others': os.path.join(download_directory, 'others')
        }
        for subdir in subdirs.values():
            os.makedirs(subdir, exist_ok=True)  # Создаем подкаталоги

        extensions = {
            'photos': ('.jpg', '.jpeg', '.png', '.gif', '.heic', '.thm'),
            'videos': ('.mp4', '.mov'),
        }
    else:
        extensions = {
            'photos': ('.jpg', '.jpeg', '.png', '.gif', '.heic', '.thm') if file_type == 'photos' else (),
            'videos': ('.mp4', '.mov') if file_type == 'videos' else ()
        }

    total_photos = sum(count_photos_in_directory(os.path.expanduser(iphone_directory))[0] for ext in extensions.values())
    
    if total_photos == 0:
        print("Нет файлов для скачивания.")
        deactivate_iphone()
        return

    print(f"Начинаем скачивание {total_photos} файлов...")
    
    downloaded_photos = 0

    for root, dirs, files in os.walk(os.path.expanduser(iphone_directory)):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions['photos']):
                destination = os.path.join(download_directory, 'photos', file)
            elif any(file.lower().endswith(ext) for ext in extensions['videos']):
                destination = os.path.join(download_directory, 'videos', file)
            else:
                destination = os.path.join(download_directory, 'others', file)

            shutil.copy2(os.path.join(root, file), destination)  # Копируем файл
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
