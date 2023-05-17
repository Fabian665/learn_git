import visitors


def main():
    functions_list = [f for f in visitors.__dict__.values() if hasattr(f, '__call__')]
    for function in functions_list[1:]:
        function()

    with open("visitors.txt", "r") as file:
        print(file.read())


if __name__ == '__main__':
    main()
