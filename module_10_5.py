# Импортируем необходимые библиотеки
# time для измерения времени выполнения
# и Pool из multiprocessing для реализации многопроцессного подхода.
import time
from multiprocessing import Pool
# Функция read_info принимает название файла, создает пустой список all_data,
# открывает файл для чтения и считывает его построчно, добавляя каждую строку в список.
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data
# Создаем список названий файлов, которые нужно прочитать.
filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
# Используем линейный вызов измеряя время выполнения цикла считывающего данные из файлов линейно.
    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"{linear_time} (линейный)")
# Для многопроцессного вызова используем контекстный менеджер with и объект Pool, чтобы
# запустить функцию read_info параллельно для всех файлов.
# Измеряем время выполнения.
    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"{multiprocessing_time} (многопроцессный)")
