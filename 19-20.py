from functools import lru_cache
import time
import psutil
import os
def transition(state):
    return state

def main_menu():
    print("Чем я могу помочь?")
    print("1. Задание 1: Повернуть матрицу на 90 градусов по часовой стрелке")
    print("2. Задание 2: Повернуть матрицу на 90 градусов против часовой стрелки")
    print("3. Выход")
    choice = input()
    if choice == 'Привет':
        print("Привет, выбери опцию")
        return 'main_menu'
    elif choice == '1' or choice == "Задание 1":
        return 'task1'
    elif choice == '2' or choice == "Задание 2":
        return 'task2'
    elif choice == '3' or choice == "Выход":
        return 'exit'
    else:
        print("Извините, я не уверен, как ответить на это.")
        return 'main_menu'

def task1():
    print("Задание 1: Повернуть матрицу на 90 градусов по часовой стрелке")
    matrix = get_matrix_input()
    rotated_matrix = rotate_matrix_clockwise(matrix)
    print("Повернутая матрица:")
    print_matrix(rotated_matrix)
    return 'main_menu'

def task2():
    print("Задание 2: Повернуть матрицу на 90 градусов против часовой стрелки")
    matrix = get_matrix_input()

    process = psutil.Process(os.getpid())
    start_time = time.time()
    start_memory = process.memory_info().rss

    rotated_matrix = rotate_matrix_counterclockwise(matrix)
    print("Повернутая матрица:")
    print_matrix(rotated_matrix)

    end_time = time.time()
    end_memory = process.memory_info().rss
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")
    print(f"Потребление памяти: {(end_memory - start_memory) / 1024:.2f} КБ")
    
    return 'main_menu'

def get_matrix_input():
    rows = int(input("Введите количество строк: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Введите элементы строки {i+1} через пробел: ").split()))
        matrix.append(row)
    return matrix

def rotate_matrix_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_matrix_counterclockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def run(state):
    state_handlers = {
        'main_menu': main_menu,
        'task1': task1,
        'task2': task2
    }
    while state != 'exit':
        state = state_handlers[state]()

if __name__ == "__main__":
    run('main_menu')
