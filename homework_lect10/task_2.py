# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_num_one():
    # Тест на одно число
    assert all_division(5, ) == 5


@pytest.mark.smoke
def test_num_n():
    # Тест с маркой smoke
    # Тест на несколько чисел, содержащих отрицательное
    assert all_division(5, -2, 4) == -0.625


def test_first_zero():
    # Тест на несколько чисел, первое из которых 0
    assert all_division(0, 1, 2) == 0


def test_div_by_string():
    # Тест деления на строку
    with pytest.raises(TypeError) as err:
        all_division(1, 'cat', 7)
    assert err.value.args[0] == "unsupported operand type(s) for /=: 'int' and 'str'"


@pytest.mark.smoke
def test_zero():
    # Тест с маркой smoke
    # Тест деления на 0
    with pytest.raises(ZeroDivisionError) as ex_zero:
        all_division(1, 0, 7)
    assert ex_zero.value.args[0] == 'division by zero'
