def main():
    full_name = input("Please enter your first, middle, and last name: ")
    name = full_name.split()

    for string in name:
        print(string[0].upper(), sep='', end='')
        print('.', sep = '', end = '')

if __name__ == '__main__':
    main()