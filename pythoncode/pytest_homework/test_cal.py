import pytest
import yaml

from pythoncode.pytest_homework.Calculator import Cal


def data(operator):
    with open("data/testdata.yml", 'r') as f:
        print(f)
        data = yaml.safe_load(f)
        if operator == "add":
            d = data["add"]
        if operator == "sub":
            d = data["sub"]
        if operator == "multi":
            d = data["multi"]
        if operator == "div":
            d = data["div"]
        return d
class Test_cal:
    @pytest.mark.parametrize("a,b,result",data("add"))
    def test_add(self,cal_fixture,a,b,result):
        assert Cal().add(a,b) == result

    @pytest.mark.parametrize("a,b,result", data("sub"))
    def test_sub(self,cal_fixture,a,b,result):
        assert Cal().sub(a, b) == result

    @pytest.mark.parametrize("a,b,result", data("multi"))
    def test_multi(self,cal_fixture,a,b,result):
        assert Cal().multi(a, b) == result

    @pytest.mark.parametrize("a,b,result", data("div"))
    def test_div(self,cal_fixture,a,b,result):
        assert Cal().div(a, b) == result
