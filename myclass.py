class Name:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Person(Name):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    def get_email(self):
        return self.email


class Dog(Name):
    def __init__(self, name):
        super().__init__(name)


if __name__ == '__main__':
    tom = Person("Tom", "tom@tom.com")
    hachi = Dog("Hachi")

    print(tom.get_name())
    print(tom.get_email())
    print(hachi.get_name())
