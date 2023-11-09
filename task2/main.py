import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

"""ФУНКЦИЯ ДЕСЕРЕАЛИЗУЕТ CSV ФАЙЛ И ЗАПИСЫВАЕТ В JSON ФОРМАТ"""

def task() -> None:
    with open(INPUT_FILENAME) as f:
        csv_data = csv.DictReader(f)
        json_data = json.dumps([row for row in csv_data], indent=4)

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
