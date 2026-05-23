import threading
from concurrent.futures.thread import ThreadPoolExecutor
import time

# Глобальный счетчик, который будут изменять все потоки
shared_counter = 0
counter_lock = threading.Lock()


def increment_shared_counter(n):
    """Функция увеличивает общий счетчик n раз"""
    global shared_counter
    for _ in range(n):
        with counter_lock:
            # Читаем текущее значение
            current_value = shared_counter
            # Имитируем небольшую задержку для увеличения вероятности гонки
            time.sleep(0.000001)
            # Записываем увеличенное значение
            shared_counter = current_value + 1

if __name__ == "__main__":
    n = 1000
    num_threads = 4

    # Сбрасываем счетчик
    shared_counter = 0

    print(f"Ожидаемый результат: {n * num_threads}")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Каждый поток будет увеличивать счетчик n раз
        futures = [executor.submit(increment_shared_counter, n) for _ in range(num_threads)]
        # Ждем завершения всех потоков
        for future in futures:
            future.result()

    print(f"Фактический результат: {shared_counter}")
    print(f"Потеряно инкрементов: {(n * num_threads) - shared_counter}")