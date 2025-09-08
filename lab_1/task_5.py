# Проведите эксперимент, сравнивающий производительность оператора in для множеств и
# списков. Покажите их поведение при помощи графика зависимости времени от количества входных данных.

from time import time
import matplotlib.pyplot as plt

# Использует хэщ-таблицу, что помогает быстрее находить элемент в списке
def in_set(n):
    s = set(range(n))  
    _ = -1 in s  
    return 


# Перебирает весь список, вследствие чего поиск замедляется
def in_list(n):
    lst = list(range(n)) 
    _ = -1 in lst  
    return 


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
        time_one = measure_algorithm_time(in_set, size)
        time_two = measure_algorithm_time(in_list, size)

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