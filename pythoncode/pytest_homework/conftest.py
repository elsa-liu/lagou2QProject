import pytest

@pytest.fixture(scope='function')
def cal_fixture():
    print("开始计算")
    yield cal_fixture
    print("计算结束")