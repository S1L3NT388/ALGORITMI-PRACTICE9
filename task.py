import time
import random
import bisect

def generate_random_array(size: int) -> list[int]:
    return [random.randint(-10000, 10000) for _ in range(size)]


def find_6th_by_sorting(arr: list[int]) -> int:
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[5]


def find_6th_by_fixed_buffer(arr: list[int]) -> int:
    top_6 = sorted(arr[:6])

    for num in arr[6:]:
        if num > top_6[0]:
            bisect.insort(top_6, num)
            top_6.pop(0)

    return top_6[0]


def find_6th_by_repeated_max(arr: list[int]) -> int:
    data = arr.copy()
    min_possible = -10001
    last_max = None

    for _ in range(6):
        max_idx = 0
        max_val = data[0]
        for i in range(1, len(data)):
            if data[i] > max_val:
                max_val = data[i]
                max_idx = i

        last_max = max_val
        data[max_idx] = min_possible

    return last_max


def measure_time(func, data: list[int]) -> float:
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return (end - start) * 1000.0


def benchmark_all():
    test_sizes = [10_000, 100_000, 1_000_000, 10_000_000]

    print("=== Практична робота №9: Порівняння ефективності алгоритмів ===")
    print(f"{'Розмір':>12} | {'Спосіб 1 (Сортування)':^24} | {'Спосіб 2 (Масив)':^24} | {'Спосіб 3 (Максимуми)':^24}")
    print("-" * 92)

    for size in test_sizes:
        runs_s1, runs_s2, runs_s3 = [], [], []

        for _ in range(3):
            dataset = generate_random_array(size)

            t1 = measure_time(find_6th_by_sorting, dataset)
            t2 = measure_time(find_6th_by_fixed_buffer, dataset)
            t3 = measure_time(find_6th_by_repeated_max, dataset)

            runs_s1.append(t1)
            runs_s2.append(t2)
            runs_s3.append(t3)

        avg_s1 = sum(runs_s1) / 3
        avg_s2 = sum(runs_s2) / 3
        avg_s3 = sum(runs_s3) / 3

        str_s1 = f"{avg_s1:.1f} ({runs_s1[0]:.0f} {runs_s1[1]:.0f} {runs_s1[2]:.0f})"
        str_s2 = f"{avg_s2:.1f} ({runs_s2[0]:.0f} {runs_s2[1]:.0f} {runs_s2[2]:.0f})"
        str_s3 = f"{avg_s3:.1f} ({runs_s3[0]:.0f} {runs_s3[1]:.0f} {runs_s3[2]:.0f})"

        print(f"{size:>12,d} | {str_s1:^24} | {str_s2:^24} | {str_s3:^24}".replace(",", " "))


if __name__ == "__main__":
    benchmark_all()