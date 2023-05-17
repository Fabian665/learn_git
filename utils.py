def append_decorator(func):
    def wrapper():
        result = func()
        with open("visitors.txt", "a") as file:
            file.write(result + '\n')
    return wrapper
