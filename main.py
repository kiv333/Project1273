per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада : "))
deposit = []
deposit.append(round((per_cent['ТКБ']/100)*money))
deposit.append(round((per_cent['СКБ']/100)*money))
deposit.append(round((per_cent['ВТБ']/100)*money))
deposit.append(round((per_cent['СБЕР']/100)*money))
print("deposit =", deposit)
print("Максимальная сумма:", max(deposit))
