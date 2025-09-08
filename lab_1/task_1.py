#1) Что выполняет приведенная функция?
#2) Какова вычислительная сложность алгоритма (в O-нотации)?
# Постройте график возрастания времени выполнения функции при увеличении
# входных данных.

# 5 вариант 

from time import time
import numpy as np
import matplotlib.pyplot as plt



def foo(nums): # nums - список
 for x in nums:
    if x % 2 == 0:
        return True
    else:
        return False

#foo([1])
#foo([1,2,3,4,5])
#foo([1,2,3,4,5,6,7,8,9,10])

def measure_algorithm_time(n):
    nums = np.random.randint(0,100,n)

    tic = time()
    foo(nums) # ф-ция из задания
    toc = time()

    return toc - tic


def create_performance_chart():
    input_sizes = list(range(100, 2100, 200))
    times = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        execution_time = measure_algorithm_time(size)
        times.append(execution_time)
        print(f"Размер: {size}, Время: {execution_time:.6f}s")
    
    plt.figure(figsize=(12, 8))
    plt.plot(input_sizes, times, marker='o', linewidth=2, markersize=8, color='blue')
    
    plt.title('Зависимость времени выполнения алгоритма от размера входных данных', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    create_performance_chart()

# Ответ:
# 1. Функция проверяет первую цифру на четность и сразу завершает работу из-за размер списка не имеет влияние
# на время работы программы
# 2. O(1)
