def calculate_coins(sum, coins):
    result = {}
    coins = sorted(coins, reverse=True)
    for coin in coins:
        count = sum // coin
        sum -= count * coin
        result[coin] = count
    return result

coins = [5000, 2000, 1000, 500, 200, 100, 10, 5, 2, 1]
sum = int(input("Введите сумму: "))
result = calculate_coins(sum, coins)

for coin, count in result.items():
    if count > 0:
        print(f"{count} купюр(ы) номиналом {coin}")
