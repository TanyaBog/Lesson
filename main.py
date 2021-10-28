# 1. Выяснить тип результата выражений:
result_1 = 15 * 3
result_2 = 15 / 3
result_3 = 15 * 2
result_4 = 15 ** 2

print('15 * 3 = ', result_1, type(result_1))
print('15 * / = ', result_2, type(result_2))
print('15 // 2 = ', result_3, type(result_3))
print('15 ** 2 = ', result_4, type(result_4))


# 2. Дан список:

strings = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
strings_mod = []
strings_format = []

print(strings)

for idx in range(len(strings)):
    # Проверка элемента списка на число и число со знаком
    char_detected = False
    char_t_detected = False
    string = strings[idx]
    for inx in range(len(string)):
        if inx == 0 and string[inx] == '+' or string[inx] == '-':
            char_t_detected = True
            continue

        if 48 <= ord(string[inx]) <= 57:
            char_detected = True
        else:
            char_detected = False
            break

    if char_t_detected and char_detected:
        strings[idx] = f'{strings[idx][0]}{int(strings[idx][1:]):02d}'
        quotes_t = ['"', strings[idx], '"']
        strings_mod.extend(quotes_t)
        quotes_t = ''.join(quotes_t)
        strings_format.append(quotes_t)
    elif char_detected:
        strings[idx] = f'{int(strings[idx]):02d}'
        quotes = ['"', strings[idx], '"']
        strings_mod.extend(quotes)
        quotes = ''.join(quotes)
        strings_format.append(quotes)
    else:
        strings_mod.append(strings[idx])
        strings_format.append(strings[idx])

print(strings)
print(strings_mod)
strings_format = ' '.join(strings_format)
print(strings_format)

# Задание 3

SALUTE = 'Привет, {}!'

workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for worker in workers:
    print(SALUTE.format(worker.split()[-1].title()))


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