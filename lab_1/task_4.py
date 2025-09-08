# Проведите эксперимент, сравнивающий производительность оператора del для словарей и
# списков. Покажите их поведение при помощи графика зависимости времени от количества входных данных.
# 

from time import time
import numpy as np
import matplotlib.pyplot as plt

# Словари
def del_dict(n):
    d = {i: i for i in range(n)}
    for i in range(n):
        del d[i]  
    return 


# Удаление одного элемента это O(1), соответственно O(n) - удаление всего словаря
# Т.к. удаление происходит по ключу и внутренних смещений не происходит

# Списки
def del_list(n):
    lst = list(range(n))
    for i in range(n):
        del lst[0]
    return 

# Здесь же одно удаление занимает O(n), что означает что весь список будет занимать O(n)*n или же O(n**2)
# Так происходит из-за того, что все оставшиеся элементы списка смещаются после удаления одного из элементов.

def measure_algorithm_time(func, n):
    tic = time()
    func(n) 
    toc = time()

    return toc - tic

def create_performance_chart():
    input_sizes = list(range(100, 10000, 500))
    times_func_one = []
    times_func_two = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        time_one = measure_algorithm_time(del_dict, size)
        time_two = measure_algorithm_time(del_list, size)

        times_func_one.append(time_one)
        times_func_two.append(time_two)

        print(f"Размер: {size}, func_one: {time_one:.6f}s, func_two: {time_two:.6f}s")
    
    plt.figure(figsize=(12, 8))

    plt.plot(input_sizes, times_func_one, marker='o', linewidth=2, markersize=8, color='blue')
    plt.plot(input_sizes, times_func_two, marker='s', linewidth=2, markersize=8, color='red')
    
    plt.title('Сравнение времени выполнения алгоритма', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    create_performance_chart()