# -*- coding: utf-8 -*-

# Поиск индекса элемента в списке товаров

def find_index(item_list, name):
    for i, index in enumerate(item_list):
        if index == name:
            return i

    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
