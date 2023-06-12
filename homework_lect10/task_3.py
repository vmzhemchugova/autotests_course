# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result', [((5,), 5),
                                          pytest.param((5, -2, 4), -0.625, marks=pytest.mark.smoke('smoke test')),
                                          ((0, 1, 2), 0),
                                          pytest.param((1, 'cat', 7),
                                                       "unsupported operand type(s) for /=: 'int' and 'str'",
                                                       marks=pytest.mark.skip('skip test')),
                                          ((1, 0, 7), 'division by zero')])
def tests_division(args, result):
    # Тест с параметрами в @pytest.mark.parametrize
    # 2 пара smoke тест
    # 4 пару скипаем
    try:
        # Сравниваем результат
        assert all_division(*args) == result
    except Exception as err:
        # Сравниваем текст ошибки (для тестов 4-5)
        assert err.args[0] == result
