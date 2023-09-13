def count_ways_to_top(K, N):



    ways = [0] * (N + 1)


    ways[0] = 1


    for i in range(1, N + 1):
        for j in range(1, min(K, i) + 1):
            ways[i] += ways[i - j]


    return ways[N]



while True:
    try:
        K = int(input("Введіть максимальну кількість сходинок, які може подолати заєць (K): "))
        N = int(input("Введіть кількість сходинок (N): "))
        if K < 1 or N < 1:
            print("Будь ласка, введіть цілі невід'ємні числа для K та N.")
        else: break
    except ValueError:
        print("Будь ласка, введіть цілі невід'ємні числа для K та N.")


result = count_ways_to_top(K, N)
print(f"Кількість різних способів дістатися до вершини сходів: {result}")
