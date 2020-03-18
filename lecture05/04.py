"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from os import path

translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': "Четыре"
}
original_file_dict = {}
with open(f"{path.join(path.dirname(__file__), '04_task_text_original')}", encoding="utf-8") as file_descriptor:
    with open(f"{path.join(path.dirname(__file__), '04_task_text_new')}",
              'a+', encoding="utf-8") as new_file_descriptor:
        for line in file_descriptor:
            new_line = f"{translate_dict[line.split()[0]]} - {line.split()[2]}"
            print(new_line)
            new_file_descriptor.write(f"{new_line}\n")
