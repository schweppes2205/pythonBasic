"""
2. Создать текстовый файл (не программно), сохранить в нем несколько
строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

from os import path

with open(f"{path.join(path.dirname(__file__), '02_task_text')}", "r") as file_descriptor:
    for i, line in enumerate(file_descriptor):
        print(f"line number {i + 1}, words count: {len(line.split())}")
    print(f"Lines amount {i+1}")
