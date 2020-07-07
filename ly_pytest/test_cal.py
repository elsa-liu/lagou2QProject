from ly_pytest import Calcu_simple
import pytest
import yaml
with open(datas/cal.yaml) as f:
    data = yaml.safe_load(f)
    print(data)
class Test_add:
    @pytest.mark.parametrize('a,b,result',[(1,1,2),(2,3,5),(1,3,4)],ids=['s','ss','sss'])

    def test_add1(self,a,b,result):
        #self.cal = Calcu_simple()
        print("测试 相加1")
        assert result == Calcu_simple.add(a,b)
