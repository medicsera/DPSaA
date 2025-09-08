# 1) Реализуйте два разных алгоритма решения задачи.
# 2) Укажите их асимптотическую сложность.
# 3) Покажите их поведение при помощи графика зависимости времени от количества
# входных данных.

# 5 вариант

from time import time
import numpy as np
import matplotlib.pyplot as plt

array_number = np.random.randint(0, 99, 20)

# Дана строка. Определить какая буква встречается чаще всего.

# 1.

# Не эффективный, так как приходится каждый раз проходиться по строке,
# чтобы посчитать сколько раз встречается один символ
def algorithm_1(s):
    max_char = None
    max_count = 0
    for char in set(s):  
        count = s.count(char)  
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

# Более эффективный, так как проходка один раз всего,
# за которую считается количество повторений каждого символа
def algorithm_2(s):
    freq = {}
    for char in s: 
        freq[char] = freq.get(char, 0) + 1
    max_char = max(freq, key=freq.get)
    return max_char

# 2.

# Первый (algorithm_1) имеет O(k*n), где k количество уникальных символов.
# Второй (algorithm_2) имеет O(n), так как проходка осуществляется единожды.

# 3

def measure_algorithm_time(func, n):
    array = ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), n))
    
    tic = time()
    func(array) 
    toc = time()
    
    return toc - tic


def create_performance_chart():
    input_sizes = list(range(100, 10000, 500))
    times_algorithm_1 = []
    times_algorithm_2 = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        time_1 = measure_algorithm_time(algorithm_1, size)
        time_2 = measure_algorithm_time(algorithm_2, size)

        times_algorithm_1.append(time_1)
        times_algorithm_2.append(time_2)

        print(f"Размер: {size}, algorithm_1: {time_1:.6f}s, algorithm_2: {time_2:.6f}s")
    
    plt.figure(figsize=(12, 8))

    plt.plot(input_sizes, times_algorithm_1, marker='o', linewidth=2, markersize=8, color='blue')
    plt.plot(input_sizes, times_algorithm_2, marker='s', linewidth=2, markersize=8, color='red')
    
    plt.title('Сравнение времени выполнения алгоритма', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    create_performance_chart()