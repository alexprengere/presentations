
def main():
    with open('test.b', 'rb') as f:
        while True:
            s = f.read(3)
            if s == '':
                break
            print(repr(s))


if __name__ == '__main__':
    main()
