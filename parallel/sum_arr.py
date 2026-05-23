import threading
from multiprocessing import Pool
from time import time
import os
import random
import argparse
import concurrent.futures


def sequential_sum(arr: list[int]) -> int:
    """Последовательное вычисление суммы массива"""
    return sum(arr)
    # total = 0
    # for num in arr:
    #     total += num
    # return total

def parallel_sum_threads(arr: list[int], num_threads: int = 4) -> int:
    """Параллельное вычисление суммы с использованием потоков"""
    if len(arr) == 0:
        return 0

    chunk_size = len(arr) // num_threads
    if chunk_size == 0:
        return sequential_sum(arr)

    chunks = []
    for i in range(num_threads):
        start = i * chunk_size
        end = len(arr) if i == num_threads - 1 else start + chunk_size
        chunks.append(arr[start:end])

    results = [0] * num_threads

    def sum_chunk(chunk, index):
        results[index] = sequential_sum(chunk)

    threads = []
    for i, chunk in enumerate(chunks):
        if chunk:
            thread = threading.Thread(target=sum_chunk, args=(chunk, i))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return sequential_sum(results)

def parallel_sum_processes(arr: list[int], num_processes: int = 4) -> int:
    """Параллельное вычисление суммы с использованием процессов"""
    if len(arr) == 0:
        return 0

    chunk_size = len(arr) // num_processes
    if chunk_size == 0:
        return sequential_sum(arr)

    chunks = []
    for i in range(num_processes):
        start = i * chunk_size
        end = len(arr) if i == num_processes - 1 else start + chunk_size
        if start < len(arr):
            chunks.append(arr[start:end])

    with Pool(processes=num_processes) as pool:
        partial_sums = pool.map(sum, chunks)
        return sum(partial_sums)

def sum_with_threading(arr: list[int], num_processes: int) -> int:
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i+chunk_size] for i in range(num_processes)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(sum, chunks))

    return sum(results)

N = 100_000_000
ARR = [1 for i in range(N)]

if __name__ == "__main__":
    # print(sequential_sum(ARR))
    print(parallel_sum_threads(ARR, os.cpu_count() // 2 + 1))
    # print(parallel_sum_processes(ARR, 4))
    # print(sum(ARR))
    # print(sum_with_threading(ARR, os.cpu_count() // 2 + 1))