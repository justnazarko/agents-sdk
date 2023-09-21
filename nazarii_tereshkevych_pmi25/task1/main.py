def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Будь ласка, введіть ціле число більше або рівне 1.")
            else:
                return value
        except ValueError:
            print("Будь ласка, введіть ціле число більше або рівне 1.")

def count_ways_to_top(K, N):
    ways = [0] * (N + 1)
    ways[0] = 1

    for i in range(1, N + 1):
        for j in range(1, min(K, i) + 1):
            ways[i] += ways[i - j]

    return ways[N]


        K = validate_input("Введіть максимальну кількість сходинок, які може подолати заєць (K): ")
        N = validate_input("Введіть кількість сходинок (N): ")

result = count_ways_to_top(K, N)
print(f"Кількість різних способів дістатися до вершини сходів: {result}")