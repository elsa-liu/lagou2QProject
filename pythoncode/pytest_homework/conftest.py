import pytest
import yaml


@pytest.fixture(scope='function')
def cal_fixture():
    print("开始计算")
    yield cal_fixture
    print("计算结束")


def pytest_collection_modifyitems(session, config, items):
    pass


def pytest_addoption(parser):
    mygroup = parser.getgroup("my_liuy")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    mygroup.addoption("--env1",
                      default='test',
                      dest='opp',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == "test":
        print("---------这是测试数据---------")
        with open("data/test.yml", "r") as f:
            data = yaml.safe_load(f)
    elif myenv == "dev":
        print("---------这是dev数据---------")
        with open("data/dev.yml", "r") as f:
            data = yaml.safe_load(f)
    elif myenv == "st":
        print("---------这是st数据---------")
        with open("data/st.yml", "r") as f:
            data = yaml.safe_load(f)

    return data
