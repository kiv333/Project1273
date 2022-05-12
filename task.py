per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада : "))
deposit = []
for value in per_cent.values():
    deposit.append(round((value/100)*money))
print("deposit =", deposit)
print("Максимальная сумма:", max(deposit))