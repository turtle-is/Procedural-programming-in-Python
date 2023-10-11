# -*- coding: utf-8 -*-

# Описание
# У вас имеется информационный объем дискеты, равный 1,44 Мб, а также параметры книги, такие как количество страниц, число строк на странице и количество символов в строке.
# Ваша задача — рассчитать, сколько одинаковых книг можно поместить на дискету, и вывести результат на экран.

total_size = 1.44 * 1024 * 1024
page_count = 100
line_count = 50
char_count_in_line = 25
size_one_char = 4

size_one_book = page_count * line_count * char_count_in_line * 4

count_books = int(total_size // size_one_book)

print("Количество книг, помещающихся на дискету:", count_books)