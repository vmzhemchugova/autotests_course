# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    # Получаем аргументы первой марки теста
    result = test.pytestmark[0].args
    # Выводим на печать без скобок tuple
    print('\n' + str(result)[1: -1])
