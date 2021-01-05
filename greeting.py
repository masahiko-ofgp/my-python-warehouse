def hello(name=None):
    if name is None:
        return "Hello, world!!"
    else:
        return f"Hello, {name}!!"

if __name__ == '__main__':
    print(hello())
    print(hello("Tom"))
