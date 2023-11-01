# -*- coding: utf-8 -*-

# Частотный анализ букв в тексте

def count_letters(txt):
    txt_dict = {}
    for char in txt:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower in txt_dict:
                txt_dict[char_lower] += 1
            else:
                txt_dict[char_lower] = 1
    return txt_dict


def calculate_frequency(txt_dict):
    count = sum(txt_dict.values())
    aver_txt_dict = {}

    for char, i in txt_dict.items():
        aver_txt_dict[char] = round(i / count, 2)

    return aver_txt_dict



main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

my_letters = count_letters(main_str)
my_frequency = calculate_frequency(count_letters(main_str))

for letter, frequency in my_frequency.items():
    print(f"{letter}: {format(frequency, '.2f')}")