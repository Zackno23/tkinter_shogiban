class Cat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SuperCat(Cat):
    def __init__(self, name, age, function):
        super(SuperCat, self).__init__(name, age)
        self.function = function


sample1 = Cat("ちゃちゃ", 12)
sample2 = SuperCat("ごん", "めっちゃ飛ぶ", "死ぬほど飛ぶ")

print(sample2.name, sample2.function)
