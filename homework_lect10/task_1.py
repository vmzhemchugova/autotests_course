# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name():
    # Формируем алфавит из доступных для использования символов
    alphabet = string.ascii_lowercase
    while True:
        # Генерируем с помощью random 2 слова из букв сформированного алфавита длиной от 1 до 15
        word_one = ''.join(random.choice(alphabet) for i in range(random.randint(1, 15)))
        word_two = ''.join(random.choice(alphabet) for i in range(random.randint(1, 15)))
        yield f'{word_one} {word_two}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
