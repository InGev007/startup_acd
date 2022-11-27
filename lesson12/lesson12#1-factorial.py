import concurrent.futures
import time


# Список чисел для вычесления факториала
numbers = range(5000, 6000)


def factorial(n: int):
    factorials = 1
    for i in range(2, n + 1):
        factorials *= i
    return factorials


def main():
    # while True:
        # n = int(input("Введите число для вычесления факториала:"))
        # time_start = time.time()
        # answer = factorial(n)
        # print("Время выполнения"+str((time.time()-time_start)))

    time_start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(factorial, i)
    pr_time = time.time() - time_start
    print("Время выполнения пула процессов:" + str(pr_time))

    time_start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(factorial, i)
    th_time = time.time() - time_start
    print("Время выполнения пула потоков:" + str(th_time))
    if pr_time < th_time:
        print("Более скоростной в данном случае ProcessPoolExecutor")
    else:
        print("Более скоростной в данном случае ThreadPoolExecutor")


if __name__ == '__main__':
    main()