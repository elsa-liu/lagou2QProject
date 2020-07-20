import yaml


def data():
    with open("data/testdata.yml", 'r') as f:
        print(f)
        data = yaml.safe_load(f)
        data_add = data["add"]
        print (data_add)
        return data_add


data()