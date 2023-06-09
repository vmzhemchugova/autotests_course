# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

import re

with open("test_file/task1_data.txt", 'r', encoding='utf-8') as file:
    with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as res_file:
        file_content = file.readlines()
        # Формируем список строк, удаляя из них цифры, и записываем полученный результат в файл task1_answer.txt
        res_file.writelines(re.sub('[0-9]', '', file_line) for file_line in file_content)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
