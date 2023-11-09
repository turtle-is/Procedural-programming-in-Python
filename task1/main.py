import json

INPUT_FILE = "input.json"

"""ФУНКЦИЯ СЧИТЫВАЕТ JSON ФАЙЛ И СЧИТАЕТ СУММЫ ПРОИЗВЕДЕНИЙ ПО КЛЮЧАМ "score" и "weight" """

def task() -> float:
    with open(INPUT_FILE) as f:
        data = json.load(f)

    list_multiplication = [item["score"] * item["weight"] for item in data]

    return round(sum(list_multiplication), 3)


print(task())
