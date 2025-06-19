import os
import time


def wait_for_file(download_dir, extension=".exe", timeout=30):
    """
    Ожидает появления файла с нужным расширением в указанной директории

    :param download_dir: путь к папке загрузки
    :param extension: расширение ожидаемого файла (например, .exe)
    :param timeout: максимальное время ожидания
    :return: полный путь к файлу
    :raises TimeoutError: если файл не найден за timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        files = os.listdir(download_dir)
        for file in files:
            if file.endswith(extension) and not file.endswith(".crdownload"):
                return os.path.join(download_dir, file)
        time.sleep(0.5)

    raise TimeoutError(f"Файл с расширением {extension} не найден за {timeout} секунд")