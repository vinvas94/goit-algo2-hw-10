import random
import time
import matplotlib.pyplot as plt
import numpy as np

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr) 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)

sizes = [10_000, 50_000, 100_000, 500_000]
results_deterministic = []
results_randomized = []

for size in sizes:
    test_array = [random.randint(1, 1_000_000) for _ in range(size)]
    print(f"Processing size: {size}")
    time_deterministic = measure_time(deterministic_quick_sort, test_array)
    time_randomized = measure_time(randomized_quick_sort, test_array)
    results_deterministic.append(time_deterministic)
    results_randomized.append(time_randomized)
    print(f"   Рандомізований QuickSort: {time_randomized:.4f} секунд")
    print(f"   Детермінований QuickSort: {time_deterministic:.4f} секунд")

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(sizes, results_randomized, marker='o', linestyle='-', label='Рандомізований QuickSort')
plt.plot(sizes, results_deterministic, marker='o', linestyle='-', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння рандомізованого та детермінованого QuickSort')
plt.legend()
plt.grid(True)
plt.yticks(np.arange(0, 3.5, 0.5))
plt.show()

# Висновки
print("Результати аналізу швидкодії:")
for i, size in enumerate(sizes):
    print(f"Масив {size} елементів: Детермінований = {results_deterministic[i]:.5f} сек, Рандомізований = {results_randomized[i]:.5f} сек")