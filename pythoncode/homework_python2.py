import yaml
class Animal:
    def __init__(self,name,color,age,gender):
        self.n = name
        self.c = color
        self.a = age
        self.g = gender

    def run(self):
        print("animal can run")

    def call(self):
        print("animal can call")

class Cat(Animal):
    def __init__(self,name,color,age,gender,fur="short"):
        Animal.__init__(self,name,color,age,gender)
        self.f = fur

    def catch_mouse(self):
        print(f"猫猫的名字叫{self.n}，颜色是{self.a}，年龄是{self.c}岁，性别是{self.g}，毛发为{self.f} ,can catch mouse.")
    def call(self):
        print("can miaomiaomiao")

class Dog(Animal):
    def __init__(self,name,color,age,gender,fur="long"):
        Animal.__init__(self,name,color,age,gender)
        self.f = fur

    def watch_door(self):
        print(f"狗狗的名字叫{self.n}，颜色是{self.a}，年龄是{self.c}岁，性别是{self.g}，毛发为{self.f} ,can watch door.")


    def call(self):
        print("can wangwangwan")

if __name__ == '__main__':
    with open (r"data/animal.yaml","r") as f:
        datas=yaml.safe_load(f)

        data_cat = datas["cat"]
        data_dog = datas["dog"]
        print(data_cat)

        miaomiao = Cat(data_cat["name"],data_cat["age"],data_cat["color"],data_cat["gender"])
        miaomiao.catch_mouse()
        #
        wangwang = Dog(data_dog["name"],data_dog["age"],data_dog["color"],data_dog["gender"])
        wangwang.watch_door()




