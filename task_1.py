# -*- coding: utf-8 -*-

# Финансовая подушка безопасности: 
#    Планирование будущего

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_month = 0

money_capital -= spend - salary

while money_capital >= 0:
    spend += spend * increase
    money_capital -= spend - salary
    count_month += 1


print("Количество месяцев, которое можно протянуть без долгов:", count_month)