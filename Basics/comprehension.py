#print([num for num in range(1, 101) if num % 3 == 0])

total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}

fizzbuzzes = { key: set(value) for key, value in fizzbuzzes.items() }

fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz']) }

print(fizzbuzzes)

