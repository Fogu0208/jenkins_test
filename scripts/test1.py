import allure
import pytest


def add(x, y):
    return x + y


@allure.feature("加法")
class TestAdd:

    @allure.story("正数相加")
    def test01_add(self):
        assert add(1, 2) == 3

    @allure.story("负数相加")
    def test02_add(self):
        assert add(-10, 20) == 10

    @pytest.mark.parametrize("x, y, expect", [(0, 0, 0), (5, 5, 10), (-1, -1, -2)])
    def test03_add_multi(self, x, y, expect):
        assert add(x, y) == expect