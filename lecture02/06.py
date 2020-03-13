"""
6. *Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об отдельном
товаре. В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def fill_product_db(record_number=1, db=[]):
    while True:
        db_fields = ["name", "price", "amount", "measure"]
        new_dict = {}
        for field in db_fields:
            new_dict[field] = input(f"Please enter product {field}: ")
        db.append((record_number, new_dict))
        print("Current product DB contains the next data:")
        print(*db, sep="\n")
        if input("You want some more? (yes/no) ") == "yes":
            record_number += 1
            continue
        else:
            break
    return db


product_db = [
    (1, {"name": "computer", "price": 20000, "amount": 5, "measure": "unit"}),
    (2, {"name": "printer", "price": 6000, "amount": 2, "measure": "unit"}),
    (3, {"name": "scanner", "price": 2000, "amount": 7, "measure": "unit"})
]
print("Current product DB contains the next data:")
print(*product_db, sep="\n")
user_answer = input("Please enter '1' if you want to use existing data, '2' if you want to add, '3' if you want to "
                    "enter new data: ")
if user_answer == "1":
    pass
if user_answer == "2":
    product_db = fill_product_db(4, product_db)
elif user_answer == "3":
    product_db = fill_product_db()
else:
    print("1, 2 or 3 next time please.")
    exit()
analytics = {"name": [], "price": [], "amount": [], "measure": []}
for field in analytics.keys():
    for product in product_db:
        analytics[field].append(product[1][field])
print(analytics)
