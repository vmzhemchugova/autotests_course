# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("time_start_end_log")
class TestDiv:
    # Класс с фикстурой time_start_end_log
    def all_division(*arg1):
        division = arg1[1]
        for i in arg1[2:]:
            division /= i
        return division

    def test_num_one(self):
        assert self.all_division(5, ) == 5

    def test_num_n(self):
        assert self.all_division(5, -2, 4) == -0.625

    def test_first_zero(self):
        assert self.all_division(0, 1, 2) == 0

    def test_div_by_string(self, time_exec_log):
        # Тест с фикстурой time_exec_log
        with pytest.raises(TypeError) as err:
            self.all_division(1, 'cat', 7)
        assert err.value.args[0] == "unsupported operand type(s) for /=: 'int' and 'str'"

    def test_zero(self):
        with pytest.raises(ZeroDivisionError) as ex_zero:
            self.all_division(1, 0, 7)
        assert ex_zero.value.args[0] == 'division by zero'
