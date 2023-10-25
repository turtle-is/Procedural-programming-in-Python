# -*- coding: utf-8 -*-

# Продолжение финансового планирования

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

pillow_size = 0
pillow_size+= spend - salary

for i in range(9):
    spend += spend * increase
    pillow_size+= spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(pillow_size))
