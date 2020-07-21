import pytest
import yaml

from pythoncode.pytest_homework.Calculator import Cal

# def data(operator):
#     with open("data/testdata.yml", 'r') as f:
#         print(f)
#         data = yaml.safe_load(f)
#         if operator == "add":
#             d = data["add"]
#         elif operator == "sub":
#             d = data["sub"]
#         elif operator == "multi":
#             d = data["multi"]
#         elif operator == "div":
#             d = data["div"]
#         return d

with open("data/testdata.yml", "r") as f:
    datas = yaml.safe_load(f)


class Test_cal:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,result", datas["add"])
    @pytest.mark.dependency(name="add")
    def check_add(self, cal_fixture, a, b, result):
        assert Cal().add(a, b) == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,result", datas["sub"])
    @pytest.mark.dependency(depends=["add"])
    def check_sub(self, cal_fixture, a, b, result):
        assert Cal().sub(a, b) == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,result", datas["multi"])
    @pytest.mark.dependency(name="multi")
    def test_multi(self, cal_fixture, a, b, result):
        assert Cal().multi(a, b) == result

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,result", datas["div"])
    @pytest.mark.dependency(depends=["multi"])
    def test_div(self, cal_fixture, a, b, result):
        assert Cal().div(a, b) == result
    # def test_div(self):
    #     assert Cal().div(2,0) == 9
