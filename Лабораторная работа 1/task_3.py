# -*- coding: utf-8 -*-

# Описание:
# У вас есть список players, который содержит имена игроков.
# Вам необходимо определить общее количество игроков в списке и затем с использованием слайсирования разделить игроков на две равные команды.
# Распечатайте каждую команду участников на отдельной строке.

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players = len(list_players)
aver = int(count_players/2)
first_team = list_players[:aver]
second_team = list_players[aver:]
print(first_team)
print(second_team)