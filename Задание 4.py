# Задание 4

prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]


def prices_show(list_prices):
    for idx in range(len(list_prices)):
        price = str(float(list_prices[idx]))
        price = price.split('.')
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
        print(price, end='')
        if idx != len(prices) - 1:
            print(end=', ')
    print(end='\n')


# A

print('По заданию А:')
prices_show(prices)

# B

print('По заданию B:')
prices_show(prices)
print('Доказательство: id объекта до сортировки:', id(prices))
prices.sort()
prices_show(prices)
print('Доказательство: id объекта после сортировки:', id(prices))

# C

print('По заданию C:')
new_prices = sorted(prices, reverse=True)
prices_show(new_prices)


print('По заданию D:')
new_prices = new_prices[:5]
prices_show(new_prices)